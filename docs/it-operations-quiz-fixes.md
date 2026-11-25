*** Begin Patch
*** Add File: docs/it-operations-quiz-fixes.md
+# IT Operations — Quiz fixes and rationales
+
+This document lists corrections and rationales for several answers and question wording issues discovered while preparing the "IT Operations" quiz.
+
+## Q18 — Bluetooth passcode / PIN entry
+**Reported issue:** "one needs a keyboard to type a Bluetooth passcode — I've only encountered them with keyboards, can it exists for mice or headsets?"
+
+**Correction / Note:**
+- Bluetooth pairing can use several association models: *Just Works*, *Numeric Comparison*, *Passkey Entry*, and *Out-of-Band*.  
+- **Passkey Entry** requires typing a PIN/passkey on the host device (which typically uses a keyboard), but the passkey could be typed on a phone, computer, or other host — not necessarily a physical keyboard peripheral built into the device.  
+- Many input peripherals (mice, headsets) use **Just Works** or fixed-PIN (e.g., 0000 or 1234) and may not require typing on the peripheral at all. Some legacy headsets use a fixed PIN that the host enters. Some modern devices rely on numeric comparison or out-of-band methods (e.g., NFC).
+- **Conclusion:** The statement "one needs a keyboard to type a Bluetooth passcode" is misleading. A keyboard is one way to enter a passcode on the *host*, but the pairing method depends on the device class and Bluetooth mode.
+
+## Q20 — Definition of a drive vs media
+**Reported issue:** "a drive is some hardware that does R/W operations, and you put a media inside (floppy disk, CD, etc.)."
+
+**Correction / Note:**
+- Historically: A *drive* (CD drive, floppy drive) is the hardware mechanism that reads/writes, and *media* (CD, floppy disk) is the removable physical carrier.  
+- For block devices in modern computing, the term *drive* is often used interchangeably for the physical device (HDD/SSD) or logical block device. But keep the historical distinction in wording to avoid confusion:
+  - **Drive** = hardware device (can be removable or non-removable) that performs R/W operations.
+  - **Media** = removable storage medium inserted into a drive (floppy, CD, DVD, tape).
+- **Suggested quiz wording:** "Which option distinguishes the physical hardware that performs read/write vs. the removable medium inserted into it?"
+
+## Q31 — Use of a switch vs server for LAN communication
+**Reported issue:** "one uses a switch to make computers communicate on a LAN, not a server."
+
+**Correction / Note:**
+- **Switches** operate at Layer 2 (Ethernet switching) to forward frames between ports; they enable local devices to communicate within the same LAN/broadcast domain.  
+- **Servers** provide services (DHCP, DNS, file sharing, etc.) but are not required simply to *connect* hosts at Layer 2.  
+- **Conclusion:** The correct networking device to make computers talk on a LAN (electrically/logically forward frames) is a switch (or hub — though hubs are largely obsolete). A server is optional and provides services on top of the connectivity.
+
+## Q43 — Profile transfer vs migration
+**Reported issue:** "if you move data and programs, it's not just a profile transfer, but a migration."
+
+**Correction / Note:**
+- **Profile transfer** typically refers to moving user profile data (settings, documents, user-specific configuration).
+- **Migration** is a broader term that can include moving user data, applications, system state, and configurations between machines or environments.
+- **Conclusion:** If the question describes moving both data and programs (applications), prefer the term **migration**. If only user settings/data, **profile transfer** is correct.
+
+## Q51 — Fn key vs Alt/Option and typo
+**Reported issue:** "to access the full range of keys on limited keyboard layouts, you use the Fn key, not Alt/Option (also there is a typo in the question)."
+
+**Correction / Note:**
+- Many compact keyboards expose additional keys via an **Fn** modifier (Function) that is implemented in keyboard firmware/firmware layer. **Alt/Option** are OS-level modifier keys and do not typically toggle alternate hardware layers.  
+- **Suggestion:** Correct the answer to **Fn**, and fix the typo in the question (please see suggested wording below).
+
+**Suggested wording correction:**  
+Original contains a typo — replace with:  
+> "On compact laptop keyboards, which modifier key typically enables access to alternate key functions (like F1–F12, media keys) implemented in keyboard firmware?"
+
+## Q52 & Q66 — Safe Mode troubleshooting
+**Reported issue:** "if one's computer boots in safe mode, one investigates, restarting won't usually fix the problem (see Q66 for coherence)."
+
+**Correction / Note:**
+- If a computer boots into **Safe Mode**, that typically indicates a problem with drivers, services, or startup items. The correct approach is to **investigate** (event logs, safe-mode-only drivers/services, last-known-good config, uninstall recent drivers/software), not simply keep restarting.  
+- Restarting might temporarily boot to normal mode sometimes, but safe mode suggests persistent problem; diagnosing and fixing the root cause is required (uninstall problematic drivers, check logs, run system file checks, restore points).
+- **Suggested answer/key:** "Investigate and troubleshoot the cause (drivers, services, recent changes) — simple restart is not the recommended fix."
+
+---
+
+## Suggested small wording fixes (summary)
+- Clarify Bluetooth pairing methods (Just Works vs Passkey Entry).
+- Distinguish *drive* vs *media* explicitly.
+- Replace references that imply a server is required for basic LAN connectivity with *switch*.
+- Replace "profile transfer" with "migration" when programs/applications are included.
+- Replace Alt/Option with Fn where hardware-level alternate key functions are referenced.
+- For Safe Mode questions, prefer "troubleshoot/investigate" over "restart".
+
*** End Patch

