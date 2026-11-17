# Clink Duo

A personal Clink keyboard collection by stivy73, designed for iPhone Duo.

## Add to Clink

Add **`stivy73/clink-duo`** to Clink's repositories. The repository is public and uses verified GitHub release assets.

- **Duo Split — Full-width space**: QWERT / YUIOP, ASDFG / GHJKL, and ZXCV / VBNM, with G and V duplicated for thumb reach. The space bar fills the former blank area on the right, up to Search/Return, on the letter, number and symbol pages. Letter positions and key dimensions are unchanged by this update. Central spacing is built into the layout; keep Clink's native Split keyboard option off when using it.
- **Duo Graphite**: dark solid keycaps, centered labels and rounded corners. It follows the current Clink rendering capabilities and is an approximation of the reference, not an exact copy of Apple's keyboard.
- **Duo Stivy** (optional profile): a snapshot of the author's saved Clink preferences and custom layouts. It keeps QWERTY Copy as the normal base layout and includes the updated Duo layout. Applying a profile replaces preferences: skip it when you only want to update the space bar. Theme and automation bindings are configured separately.

Installing a pack does not configure the adaptive rules for you. Existing keyboard settings and automation bindings should be kept until you choose to replace them.

## Adaptive automation

Download [duo-automation.json](https://github.com/stivy73/clink-duo/releases/latest/download/duo-automation.json) from the latest release and import it in Clink's Automations settings. The repository catalog lists themes and layouts; the automation is a separate release attachment.

1. Import/install the layout and theme into your library. If Clink applies them immediately, restore your usual saved setup before configuring the rules.
2. In **Duo — Open display (link layout and theme)**, add the Layout action and choose **Duo Split — Full-width space**; add the Theme action and choose **Duo Graphite**. Imported files may get new local identities, so the portable automation omits those references. In Appearance → Themes, turn automatic theme selection off if it overrides the rule's theme.
3. Keep **Duo — Standard keyboard** first and the open-display rule after it. Enable both and disable older rules that control the same settings.
4. The open-display rule uses a width threshold of 700 points with 24-point hysteresis, 48-point key height and a 32-point suggestions bar. Below the threshold, the saved key dimensions return and the base rule keeps the standard keyboard and compact bar.

The trigger measures available width, not hinge posture. A narrow app window on an unfolded display, or a closed phone in landscape, may behave differently from physical open/closed state.

The corrected rule was activated on Clink 2.1.0 (283), with open/closed keyboard appearances observed on the author's physical Duo using Apple developer tools. The portable version intentionally omits device-local theme/layout references, which must be selected after installation. In this Clink version, `keys.long_press_hint` uses the string `"off"`, not Boolean `false`.

## Space bar update — 17 November 2026

This update preserves the author's own settings, including 12-point key spacing, 16-point row spacing, a 0.75 hitbox scale, and 21-point bottom padding. It adds no vertical spacing changes. The only change to the existing open-display rule is its Layout selection; the normal base keyboard and the other rule actions are retained.

The new layout was imported and linked on the author's physical Duo. A tap in the newly covered right-hand space area inserted a space, and the number page was checked too. The full-width space uses the same bottom-row geometry on the symbol page.

For an existing setup, refresh the repository and install/import the updated layout. If Clink creates a new library entry, select **Duo Split — Full-width space** in the existing open-display rule and save. Keep the normal base layout selected outside the rule. Publishing a release does not itself switch the phone's active layout or rebind a rule.

## Releases

Pushes to main rebuild a manifest containing exact byte counts and SHA-256 hashes. Release asset URLs are content-addressed and immutable, so an older cached manifest still points to the correct bytes. Keep pack filenames stable to preserve update identities.

`python3 tools/build-manifest.py` rebuilds the manifest locally. No scripts run on the phone: the collection contains data packs and local automation settings only.
