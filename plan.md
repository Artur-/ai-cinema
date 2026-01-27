# Cinema App - Initial Version Plan

## Overview

Build a cinema ticket reservation app with:
- **Public React/Hilla views**: browse today's movies, view showtimes, purchase tickets
- **Admin Java/Flow views**: manage movies, screenings, and view reservations
- **Backend**: Spring Boot + Postgres + JPA
- **Tests**: TestBench UI unit tests

## Data Model

### Movie
| Field | Type | Notes |
|-------|------|-------|
| id | Long | PK, auto-generated |
| title | String | required |
| description | String | text |
| durationMinutes | Integer | required |
| genre | String | |
| posterUrl | String | nullable |

### Screening
| Field | Type | Notes |
|-------|------|-------|
| id | Long | PK, auto-generated |
| movie | Movie | ManyToOne, required |
| screeningDate | LocalDate | required |
| screeningTime | LocalTime | required |
| totalSeats | Integer | required, default 100 |

### Reservation
| Field | Type | Notes |
|-------|------|-------|
| id | Long | PK, auto-generated |
| screening | Screening | ManyToOne, required |
| customerName | String | required |
| customerEmail | String | required |
| numberOfTickets | Integer | required, min=1 |
| reservationCode | String | unique, 8-char uppercase UUID prefix |
| createdAt | LocalDateTime | auto-set on creation |

Single-screen cinema. No seat selection. Available seats = totalSeats - sum of reserved tickets.

## Dependencies to Add (pom.xml)

- `spring-boot-starter-data-jpa`
- `postgresql` (runtime)
- `spring-boot-starter-security`
- `vaadin-testbench` (test)
- `h2` (test, for in-memory test DB)

## Package Structure & Files

```
com.example/
  Application.java                          (modify: add data initializer)
  data/
    Movie.java                              (entity)
    Screening.java                          (entity)
    Reservation.java                        (entity)
    MovieRepository.java                    (JPA repo)
    ScreeningRepository.java                (JPA repo: findByScreeningDate, findByMovieIdAndScreeningDate)
    ReservationRepository.java              (JPA repo: countReservedTickets query)
  services/
    MovieService.java                       (CRUD + find movies with today's screenings)
    ScreeningService.java                   (CRUD + availability calculation)
    ReservationService.java                 (create reservation, check availability, generate code)
  endpoints/
    MovieEndpoint.java                      (@BrowserCallable @AnonymousAllowed)
    ScreeningEndpoint.java                  (@BrowserCallable @AnonymousAllowed)
    ReservationEndpoint.java                (@BrowserCallable @AnonymousAllowed)
    dto/
      MovieDto.java                         (record)
      ScreeningDto.java                     (record)
      ReservationRequest.java               (record)
      ReservationResponse.java              (record)
  security/
    SecurityConfig.java                     (extends VaadinWebSecurity)
  views/
    LoginView.java                          (Vaadin LoginForm at /login)
    admin/
      AdminLayout.java                      (AppLayout with SideNav)
      MovieAdminView.java                   (Grid + form CRUD)
      ScreeningAdminView.java               (Grid + form CRUD, ComboBox for movie)
      ReservationAdminView.java             (read-only Grid)
  data/
    DataInitializer.java                    (seeds sample data in dev)

src/main/frontend/views/
  @layout.tsx                               (minimal public layout)
  index.tsx                                 (movies showing today)
  movie/{movieId}.tsx                       (movie details + ticket purchase)

src/main/resources/
  application.properties                    (modify: add DB, JPA config)

src/test/java/com/example/
  views/admin/
    MovieAdminViewTest.java                 (TestBench UIUnitTest)
    ScreeningAdminViewTest.java             (TestBench UIUnitTest)
    ReservationAdminViewTest.java           (TestBench UIUnitTest)
  endpoints/
    MovieEndpointTest.java                  (Spring integration test)
    ReservationEndpointTest.java            (Spring integration test)
src/test/resources/
  application-test.properties              (H2 in-memory config)
```

## Security

- `SecurityConfig extends VaadinWebSecurity` with form login at `/login`
- In-memory admin user: `admin` / `admin` (v1 simplicity)
- Admin views annotated `@RolesAllowed("ADMIN")`
- Hilla endpoints annotated `@AnonymousAllowed` for public access

## Hilla Endpoints (Public API)

**MovieEndpoint:**
- `getMoviesShowingToday()` → `List<MovieDto>` - movies with at least one screening today
- `getMovieById(long id)` → `MovieDto`

**ScreeningEndpoint:**
- `getTodayScreeningsForMovie(long movieId)` → `List<ScreeningDto>` - includes availableSeats

**ReservationEndpoint:**
- `purchaseTickets(ReservationRequest)` → `ReservationResponse` - validates availability, creates reservation, returns confirmation with code

## Admin Views

- **MovieAdminView** (`/admin/movies`): Grid + form for movie CRUD (title, description, duration, genre, posterUrl)
- **ScreeningAdminView** (`/admin/screenings`): Grid + form with ComboBox<Movie>, DatePicker, TimePicker, IntegerField for seats
- **ReservationAdminView** (`/admin/reservations`): Read-only grid (code, customer, movie, date/time, tickets, created)
- **AdminLayout**: AppLayout with SideNav links + logout button

## Public React Views

- **Index** (`/`): Card grid of today's movies (poster, title, genre, duration). Click navigates to details.
- **Movie Details** (`/movie/{movieId}`): Movie info, list of today's showtimes with available seats, purchase form (name, email, quantity), confirmation dialog with reservation code.

## Infrastructure

**docker-compose.yml** at project root:
- Postgres 16 container, port 5432, database `cinema`, user `cinema`, password `cinema`
- Volume for persistent data

## Implementation Order

1. **docker-compose.yml** - Postgres container
2. **pom.xml** - add all dependencies
3. **application.properties** - database + JPA config
4. **Entities** - Movie, Screening, Reservation
5. **Repositories** - with custom queries
6. **Services** - business logic layer
7. **Security** - SecurityConfig + LoginView
8. **Admin views** - AdminLayout, MovieAdminView, ScreeningAdminView, ReservationAdminView
9. **DTOs + Hilla endpoints** - MovieEndpoint, ScreeningEndpoint, ReservationEndpoint
10. **React views** - layout, index, movie details
11. **DataInitializer** - seeds sample movies with today's screenings on startup (dev profile)
12. **Tests** - TestBench UI unit tests + endpoint integration tests

## Verification

1. Start Postgres: `docker compose up -d`
2. Run app: `./mvnw spring-boot:run`
3. Visit `http://localhost:8080/` → should show today's movies
4. Click a movie → should show showtimes and purchase form
5. Fill in name/email/quantity and purchase → should show reservation code
6. Visit `http://localhost:8080/admin/movies` → should redirect to login
7. Login with admin/admin → should show movie CRUD
8. Create/edit/delete movies and screenings via admin views
9. View reservations in admin
10. Run `./mvnw test` → all TestBench and integration tests pass
