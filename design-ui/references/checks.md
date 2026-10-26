# UI checks

## Web screens

For every changed screen, at 390, 768, 1024 and 1440 wide, in every language the project ships, light and dark where the project has both:

- **Page fit:** no sideways page scroll; long words and long names wrap or truncate with the full value available.
- **Touch:** every tap target at least 44px on the phone; rows and cards open from their whole area, with their own actions beside it.
- **Fixed bars:** bottom bars, save bars and bulk-action bars never cover one another or the content's last action.
- **Lists:** on the phone, cards (or the table the project chose for that list) showing the fields that matter; on wider screens, the table.
- **Dialogs and sheets:** fit the screen with their title and actions visible; the body scrolls, not the page.
- **Right-to-left:** text, values and icons sit at the start side; numbers and codes read left to right inside it.
- **Controls:** the project's own date picker, select and inputs, not the browser's native ones, unless the project chose native.
- **Accessibility:** read the browser's accessibility tree, not the markup: every table cell under its own header, every control named, focus order sensible, nothing hidden reachable by Tab.
- **Console:** no page errors and no hydration warnings.
- **Desktop unchanged** where the round did not mean to change it: compare screenshots before and after.

## Native app screens (iOS and Android)

On the iOS Simulator and an Android emulator, in each language and theme the change touches:

- Tap through the real flow: open, fill, save, reopen, delete. Rendering a screen is not a check.
- **Taps:** tap a row's empty space, not only its label. Small action chips must not swallow the row's tap, and the row's tap must not swallow theirs.
- **Keyboard:** fields stay visible above it, and the keyboard dismisses.
- **Back:** the system back button on Android and the in-app back on iOS go where a person expects; an open sheet closes first.
- **Failure paths:** no network, a refused save, a file that cannot be opened. Each gives a message in both languages and loses nothing typed.
- **Native pickers:** the camera, the photo library and the file picker hand their result back; check the upload landed (the row's status, the database, the storage).
- Data saved on one screen shows correctly after reopening.

Save screenshots outside the repository and look at them yourself.
