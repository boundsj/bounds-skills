# Swift for app interfaces

Start with the simplest, most static, single-threaded code that works. Add reference semantics, concurrency, or type erasure only for a reason you can name. Check the project's Swift version and build settings before applying concurrency advice.

## Model with values

- Default to `struct` and `enum`. Use a class for identity, shared mutable state, or resource lifetime.
- Model mutually exclusive screen state as one enum, such as `idle`, `loading`, `loaded(items)`, `failed(error)`, instead of several booleans and optionals that can disagree.
- Prefer `let`. A struct holding a mutable class reference is not a value; copies share the object.

## SwiftUI state ownership

Give each piece of state one owner.

| Need | Use |
| --- | --- |
| Value a view owns | `@State private var` |
| Observable model a view creates | `@State private var model = Model()` with `@Observable` |
| Child that writes a parent's value | `@Binding` |
| Bindings to an observable passed in | `@Bindable` |
| Model shared across a subtree | `.environment(model)` and `@Environment(Model.self)` |
| Observable read only | a plain property; Observation tracks what `body` reads |

- Do not copy a parent's value into a child's `@State`; it captures the first value and stops updating.
- A `@State` initializer can run each time the view is recreated, even though SwiftUI keeps the first instance. Keep model initializers cheap and load in `.task`.
- Use `ObservableObject` and `@StateObject` only for deployment targets older than iOS 17 or macOS 14.
- Give `ForEach` stable identifiers, not indices. Wrapping a view in `if` changes its identity, losing state and animations; for a property change, change the property. Avoid `AnyView`.

## Concurrency (Swift 6)

- Enable Approachable Concurrency. For app and UI targets, set Default Actor Isolation to `MainActor`. Leave general-purpose libraries `nonisolated`.
- With those settings, a nonisolated `async` function runs on its caller's actor. Mark CPU-heavy work `@concurrent` to move it off the main actor, after a profile shows a hang.
- Event callbacks are synchronous. Change state, including `withAnimation`, in the callback; start a `Task` only for the async work after it.
- Prefer `.task` or `.task(id:)` over `onAppear { Task { } }`. SwiftUI cancels the task when the view disappears or the ID changes.
- Prefer structured concurrency: `async let` for a fixed set of jobs, task groups for a dynamic set. `Task.detached` almost never.
- Cancellation is cooperative. Check `Task.isCancelled` or call `try Task.checkCancellation()` before expensive steps.
- Every `await` can interleave. After it, re-check that the result still applies, for example that a search response matches the current query, before assigning.
- Actors guarantee exclusion, not transactions or ordering. Mutate actor state in synchronous methods.
- Fix data-race errors in order: stop sharing the value, make it a `Sendable` value type, isolate it to an actor, then a `Mutex`. `@unchecked Sendable` and `nonisolated(unsafe)` are last resorts, never a way to silence warnings.
- SwiftUI closures marked `@Sendable`, such as `visualEffect` and layout methods, can run off the main actor. Capture the values they need, not `self`.

## Performance and ARC

- Keep `body` cheap: no sorting, formatting, decoding, or I/O. Precompute in the model.
- Use lazy stacks or `List` for long collections, and decode images at display size.
- Split large views so a change invalidates less.
- Profile a release build on a device with Instruments (SwiftUI, Time Profiler, Hangs, Allocations) before optimizing.
- An object can be released after its last use, not at the closing brace. Use `weak` or `unowned` only to break cycles. A long-running `Task` keeps what it captures alive until it ends; `.task` scoping handles that.

## Tests

- Use Swift Testing for new tests: `@Test`, `#expect`, `try #require`, and `@Test(arguments:)` for parameterized cases. A suite is any type that holds tests; prefer a struct or actor, though a class also works. Tests run in parallel by default.
- Test view models and state machines without SwiftUI.
- XCTest remains for UI automation (`XCUIApplication`) and performance metrics. UI tests can run `performAccessibilityAudit()`.
- Passing tests prove logic. They do not prove presentation, feel, or accessibility in use.
