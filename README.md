# Clink Duo

A personal Clink keyboard collection by stivy73, designed for iPhone Duo.

## Add to Clink

Add **`stivy73/clink-duo`** to Clink's repositories. The repository is public and uses verified GitHub release assets.

- **Duo Split — Apple-inspired**: QWERT / YUIOP, ASDFG / GHJKL, and ZXCV / VBNM, with G and V duplicated for thumb reach. Central spacing is built into the layout; keep Clink's native Split keyboard option off when using it. The blank space key remains tappable. Number and symbol pages are included.
- **Duo Graphite**: dark solid keycaps, centered labels and rounded corners. It follows the current Clink rendering capabilities and is an approximation of the reference, not an exact copy of Apple's keyboard.

Installing a pack does not configure the adaptive rules for you. Existing keyboard settings and automation bindings should be kept until you choose to replace them.

## Adaptive automation

Download [duo-automation.json](https://github.com/stivy73/clink-duo/releases/latest/download/duo-automation.json) from the latest release and import it in Clink's Automations settings. The repository catalog lists themes and layouts; the automation is a separate release attachment.

1. Import/install the layout and theme into your library. If Clink applies them immediately, restore your usual saved setup before configuring the rules.
2. In **Duo — Open display (link layout and theme)**, add the Layout action and choose **Duo Split — Apple-inspired**; add the Theme action and choose **Duo Graphite**. Imported files may get new local identities, so no device-specific IDs are published here.
3. Keep **Duo — Standard keyboard** first and the open-display rule after it. Enable both and disable older rules that control the same settings.
4. The open-display rule uses a width threshold of 700 points with 24-point hysteresis, 48-point key height and a 32-point suggestions bar. Below the threshold, the saved key dimensions return and the base rule keeps the standard keyboard and compact bar.

The trigger measures available width, not hinge posture. A narrow app window on an unfolded display, or a closed phone in landscape, may behave differently from physical open/closed state.

The corrected rule was activated on Clink 2.1.0 (283), with open/closed keyboard appearances observed on the author's physical Duo using Apple developer tools. The portable version intentionally omits device-local theme/layout references, which must be selected after installation. In this Clink version, `keys.long_press_hint` uses the string `"off"`, not Boolean `false`.

## Releases

Pushes to main rebuild a manifest containing exact byte counts and SHA-256 hashes. Release asset URLs are content-addressed and immutable, so an older cached manifest still points to the correct bytes. Keep pack filenames stable to preserve update identities.

`python3 tools/build-manifest.py` rebuilds the manifest locally. No scripts run on the phone: the collection contains data packs and local automation settings only.
