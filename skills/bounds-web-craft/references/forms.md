# Forms

A form is a conversation with a stranger who is often on a phone and in a hurry. Ask for less, accept what they give, and never lose their input.

## Labels and structure

- Every control has a visible `<label>` tied to it with `for` and `id`, or by wrapping. A placeholder is not a label: it vanishes on input, usually fails contrast, and is not reliably announced.
- Put labels above fields for scanning and narrow screens. Mark the minority: if most fields are required, label the optional ones, and vice versa.
- Group related controls with `<fieldset>` and `<legend>`, especially radio and checkbox sets.
- Hints go below the label and are linked with `aria-describedby`, so they are read with the field.
- Wrap fields in a `<form>` so Enter submits and password managers recognize it. Clicking a checkbox or radio label must toggle it; do not leave dead space between box and text.
- Ask only for what you need now. Do not ask twice for the same information in one process; prefill it or offer to reuse it (WCAG 2.2 SC 3.3.7).

## Input types and mobile keyboards

| Data | Markup |
| --- | --- |
| Email | `type="email"` `autocomplete="email"` |
| Phone | `type="tel"` `autocomplete="tel"` |
| Whole numbers, codes, PINs | `type="text"` `inputmode="numeric"` (keeps leading zeros, no spinner) |
| Amounts | `inputmode="decimal"` |
| Search | `type="search"` `enterkeyhint="search"` |
| URL | `type="url"` |
| One-time code | `autocomplete="one-time-code"` `inputmode="numeric"` |

- Reserve `type="number"` for true quantities; it adds spinners, accepts `e`, and in some browsers changes value when a focused field is scrolled over. Firefox no longer does this, so check the target browsers.
- Turn off `autocapitalize` and `autocorrect`, and set `spellcheck="false"`, on usernames, emails, codes, and identifiers.
- Use `enterkeyhint` (`next`, `done`, `send`, `search`) so the return key describes what it does.
- Input text must be at least 16px or iOS Safari zooms the page on focus. Never block zoom to work around it.

## Autofill

- Give every personal-data field its `autocomplete` token: `name`, `given-name`, `email`, `tel`, `street-address`, `postal-code`, `country`, `cc-number`, `cc-exp`, `username`, `current-password`, `new-password`. SC 1.3.5 requires this for fields that collect information about the user.
- Never block paste in password or code fields. SC 3.3.8 applies to every step of signing in, including one-time codes and second factors: no step may depend on remembering, transcribing, or solving a puzzle unless paste, autofill, or another method can stand in. At AA, recognizing objects or identifying content the user supplied is allowed.
- Check autofilled fields in both themes; style `:autofill` where browser defaults clash or become illegible.
- Do not split a single value across several boxes unless they handle paste of the whole value.

## Validation timing

- Validate a field when the user leaves it (on blur) or on submit, not on every keystroke. Until submit, do not show errors on fields the user has not reached.
- Switch a field that has shown an error to live checking: someone correcting a mistake wants confirmation without leaving the field.
- Validate format on the client for speed, and everything on the server for truth. Show server errors in the same places and style.
- Do not disable the submit button until the form is valid; the user cannot learn what is missing. Let them submit and show what to fix.

## Error messages

- Say what happened and how to fix it in plain words: "Enter a date after today", not "Invalid input" (SC 3.3.1 and 3.3.3).
- Place the message next to the field, associate it with `aria-describedby`, and set `aria-invalid="true"`. Use an icon or text along with red.
- On submit with errors, move focus to the first invalid field, or to an error summary at the top that links to each field.
- Keep everything the user entered, including after a server error or a session timeout.

## Submission

- On submit: keep the form in place, show progress in the submit button, prevent duplicate submission, and keep its width stable.
- On success: confirm in place or navigate, and announce it through a live region if the page does not change.
- On failure: keep the input, explain the failure, and say whether retrying is safe.
- Destructive or irreversible submissions need a clear confirmation naming the action, or an undo window.

## Verify

Complete the form with the keyboard only, with a screen reader, with browser autofill and a password manager, on a real phone keyboard, and with server errors forced. Record which of these were actually exercised.
