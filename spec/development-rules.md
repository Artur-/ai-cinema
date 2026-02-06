For each task
1. use Playwright to validate it works properly
2. when everything works, create UI unit tests to ensure it keeps working in the future
3. always run the tests and ensure they pass
4. alert the user if an existing test needed to be updated.

Always commit after a task is complete. Include the prompts used since the
last commit in the commit message.


Endpoint classes must use @NonNull on return value and also on generic types
when appropriate. This affects the generated TS code.
