# Concepts: Reusable Architecture

## Page objects

A page object owns selectors and user-level operations for one page. Tests should read like behavior specifications while the object absorbs selector maintenance. Keep business assertions in tests; keep interaction mechanics in the object.

## Component objects

Repeated UI such as a table, date picker, or navigation bar is a component, not a page. Compose a page from components instead of creating a deep inheritance tree.

## Fixture scope

Function scope gives isolation; session scope is appropriate for an immutable server or browser binary, not for a mutable logged-in page. A fixture that yields an object must clean it up after the yield.

## Roles and contexts

A browser context is the boundary for cookies and local storage. Create one context per role or scenario when comparing permissions. Never switch a single page between users in one test.

