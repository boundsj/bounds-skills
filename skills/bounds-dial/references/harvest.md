# Harvest and cleanup

## Leave a harvest note

Before handoff, write a short note in the saves folder, such as a README, so a later session can harvest without this conversation or this skill. Include:

- the value the tool tunes and the source the product reads it from;
- how saved fields map onto that source, including units;
- how to launch the tool and load a saved version;
- the apply, verify, and record steps below.

Keep the note current if the tool or the product's source moves.

## Apply

1. **Get the label.** Ask which saved version ships if the user has not named one. Do not assume the newest file is the choice.
2. **Read the file.** Take values from that file with a mechanical copy, such as a small script, or by having the product load the file if that was agreed. Never take values from screenshots, chat, or memory of what a control showed.
3. **Check the format.** If the file's format version or fields do not match what the product expects, stop and reconcile before applying.
4. **Verify.** Compare the product's output at the same state with the tool's output for that version, using the same comparison as the save-reload check. Pin the saved seed when randomness is involved.
5. **Record.** Use the record below.

## Record

Say which version shipped and what it was judged on:

```text
Shipped: <value> from <saves path>/<label>
Judged on: <surface>, revision <commit, plus dirty state>, size <width x height as measured>, theme <theme>, data <fixtures or real source>
Not covered: <surfaces, sizes, themes, data, or audio paths nobody judged>
```

- **Surface:** browser preview, desktop build, simulator, or a named device class. A simulator or desktop preview is not the device.
- **Revision:** the commit the user judged against, with uncommitted changes noted.
- **Measured size:** read it from the running surface, such as the window, viewport, or screen. A preset's name is not a measurement.
- **Theme and data:** which appearance and which data were on screen. Fixtures prove presentation only.
- **Audio:** whether it was heard, and on what output. A muted preview does not verify audio.

Put the record in the commit message or change description. Draft PR text or comments for the user unless posting is authorized. If the tool stays, keep a copy beside the saves.

If the product changed since the judgment in ways that touch the value, such as new content, a new theme, or a changed layout, say the judgment may not carry over. Offer to reopen the tool instead of adjusting values by guess.

## Remove or gate

Ask; the user decides.

- **Remove.** Delete the tool and its dev wiring. Saved files stay as plain data unless the user asks to delete them, but nothing can replay them now. Say that before deleting, and note the removal in the record.
- **Gate.** Keep it behind the project's development mechanism. Confirm with the project's existing release build or check that the tool is excluded or inert there. Keep the harvest note current.

Either way, confirm the product still runs from its own source of truth without the tool.
