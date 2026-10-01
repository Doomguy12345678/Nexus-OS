# Chromebook Live-Session Smoke Observation

- Reported: 2026-09-30
- Source: user-confirmed manual check
- Environment: Linux Mint live session, UEFI boot, root filesystem reported as `overlay`
- Wi-Fi: works, per user report
- Speaker playback: works, per user report
- Keyboard and touchpad: work normally, per user report
- Brightness controls: work, per user report
- Suspend/resume: works normally, per user report
- OpenGL renderer: Mesa Intel(R) UHD Graphics 600 (GLK2); direct rendering: yes, per user-reported `glxinfo -B` output
- Vulkan: not checked; `vulkaninfo` is unavailable in the live session, per user report

This records user-reported observations, not an independent lab run or a Nexus-OS qualification. Vulkan is blocked on a diagnostic tool; audio latency/routing and update/rollback remain untested.
