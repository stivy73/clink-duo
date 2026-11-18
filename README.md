# Clink Duo

A personal Clink keyboard collection by stivy73, designed for iPhone Duo.

## Add to Clink

Add **`stivy73/clink-duo`** to Clink's repositories. The repository is public and uses verified GitHub release assets.

- **Duo Split — Full-width space**: QWERT / YUIOP, ASDFG / GHJKL, and ZXCV / VBNM, with G and V duplicated for thumb reach. The space bar fills the former blank area on the right, up to Search/Return, on the letter, number and symbol pages. Letter positions and key dimensions are unchanged by this update. Central spacing is built into the layout; keep Clink's native Split keyboard option off when using it.
- **Duo Graphite**: dark solid keycaps, centered labels and rounded corners. It follows the current Clink rendering capabilities and is an approximation of the reference, not an exact copy of Apple's keyboard.
- **Duo Stivy**: the editable base profile for the closed display, with the author's current 6-point key spacing, 11-point row spacing and 45-point key height. It keeps QWERTY Copy as its normal layout.
- **Duo Aperto**: a separate profile for the open-display rule, with 12-point key spacing and 16-point row spacing. The rule then applies the Duo split layout, 48-point key height and graphite theme. The profile packs include the current normal and Duo layouts; unused older Duo layout copies are excluded to stay within Clink's repository size limit.

- **Duo Laptop**: a third independent profile, copied from the current open profile on 18 November 2026 and using the united **QWERTY Copy** layout, without the center gap. Existing open/closed profile packs are unchanged.

Installing a pack does not configure the adaptive rules for you. Importing a profile applies its preferences, so save your existing setup first. Theme and automation bindings are configured separately.

## Adaptive automation

Download [duo-automation.json](https://github.com/stivy73/clink-duo/releases/latest/download/duo-automation.json) from the latest release and import it in Clink's Automations settings. The repository catalog lists profiles, themes and layouts; the automation is a separate release attachment.

1. Import/install the layout and theme into your library. If Clink applies them immediately, restore your usual saved setup before configuring the rules.
2. In **Duo — Open display (link profile, layout and theme)**, add the **Duo Aperto** action from the Profiles category and move it to the **first position** using its up arrow. Then add the Layout action and choose **Duo Split — Full-width space**; add the Theme action and choose **Duo Graphite**. Keep the existing size and toolbar actions after the profile too. Order matters: applying a profile after the Layout action replaces the selected layout. Imported files may get new local identities, so the portable automation omits profile, layout and theme references. In Appearance → Themes, turn automatic theme selection off if it overrides the rule's theme.
3. In **Duo — Laptop portrait (link Duo Laptop profile)**, add **Duo Laptop** from Profiles and move it to the first position, before the Split keyboard action. This profile supplies the united QWERTY layout. Keep your normal **Duo Stivy** profile selected as the saved base.
4. Keep **Duo — Standard keyboard** first, the open-display rule next and the laptop rule last. Enable all three after linking the profiles. Disable older rules that control the same settings; on an already configured phone, edit the existing rules instead of importing duplicates.
5. Both internal-display rules require at least 700 points of available width, with 24-point hysteresis, and use **all** conditions: **landscape** selects the split profile; **portrait** selects the united laptop profile. The split rule retains 48-point key height and a 32-point suggestions bar. Below the width threshold, both contributions end and the saved normal profile returns.

Laptop detection uses **available width plus interface orientation**, not the hinge angle. Clink currently exposes Folded/Open, without a separate intermediate-angle condition. Any sufficiently wide internal portrait view therefore uses the laptop profile, including a fully unfolded portrait display. A narrow app window or a closed phone in landscape may behave differently from the physical posture.

The corrected rule was activated on Clink 2.1.0 (283), with open/closed keyboard appearances observed on the author's physical Duo using Apple developer tools. The portable version intentionally omits device-local profile/theme/layout references, which must be selected after installation. In this Clink version, `keys.long_press_hint` uses the string `"off"`, not Boolean `false`.

## Edit the closed keyboard independently

Keep **Duo Stivy** selected as the saved base profile (on the author's phone its existing name is **Duo - impostazioni Stivy**). Edit key size, spacing and the other profile-supported settings in Clink as usual, with profile Autosave enabled. The open-display rule temporarily applies the separate **Duo aperto** profile, then the layout and explicit overrides. When width or orientation stops matching, that contribution ends and your saved base preferences return. The rule does not select or rewrite the saved base profile.

To change the open keyboard, edit **Duo aperto**, then reselect your normal base profile before finishing. Settings explicitly supplied by the rule, such as its 48-point key height and 32-point suggestions bar, must be edited in the rule. The normal rule also keeps the suggestions bar at 32 points with no top padding; those two toolbar values remain rule-controlled.

The separated configuration was checked on the physical Duo: the open display used the split layout with extended space bar while the closed display returned to the normal keyboard. Changes on the phone remain local until you export and publish another release.

## Laptop mode — 18 November 2026

The native laptop rule applies only its separate **Duo laptop** profile while width is at least 700 points and orientation is portrait. The existing split rule now also requires landscape. The saved **Duo - impostazioni Stivy** profile remains the normal base. The three transitions were checked live on the physical Duo using Apple developer tools: internal portrait → united QWERTY, internal landscape → split layout, and closed portrait → normal keyboard.

To edit laptop preferences, select **Duo laptop** in Profiles, make changes with Autosave enabled, then reselect your normal base profile. Rule-controlled toolbar settings still apply. Phone-side edits remain local until exported and published. The native exported rule is backed up locally; the public portable rule intentionally omits its device-local profile identity and remains disabled until linked.

## Space bar update — 17 November 2026

The earlier space-bar-only update preserved the author's then-current 12-point key spacing, 16-point row spacing, 0.75 hitbox scale and 21-point bottom padding. The subsequent profile separation described above preserves the newer closed-display preferences, including 6/11-point spacing, 45-point key height and zero bottom padding. The open profile has independent 12/16-point spacing; its key height remains controlled by the rule at 48 points.

The new layout was imported and linked on the author's physical Duo. A tap in the newly covered right-hand space area inserted a space, and the number page was checked too. The full-width space uses the same bottom-row geometry on the symbol page.

For an existing setup, refresh the repository and install/import the updated layout. If Clink creates a new library entry, select **Duo Split — Full-width space** in the existing open-display rule and save. Keep the normal base layout selected outside the rule. Publishing a release does not itself switch the phone's active layout or rebind a rule.

## Releases

Pushes to main rebuild a manifest containing exact byte counts and SHA-256 hashes. Release asset URLs are content-addressed and immutable, so an older cached manifest still points to the correct bytes. Keep pack filenames stable to preserve update identities.

`python3 tools/build-manifest.py` rebuilds the manifest locally. No scripts run on the phone: the collection contains data packs and local automation settings only.
