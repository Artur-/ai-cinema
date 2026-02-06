Tech stack:
- Vaadin, admin views using Java, public views using React
- Spring Boot
- H2 DB
- JPA
- JSpecify for nullability annotations
- TestBench UI unit tests

For each task
1. use Playwright to validate it works properly
2. when everything works, create UI unit tests to ensure it keeps working in the future
3. always run the tests and ensure they pass
4. alert the user if an existing test needed to be updated.

Always commit after a task is complete. Include the prompts used since the
last commit in the commit message.


Views that are publicly available are implemented in React using Hilla
endpoints.
Views that are protected by login are implemented in Java.

Endpoint classes must use @NonNull on return value and also on generic types
when appropriate. This affects the generated TS code.
