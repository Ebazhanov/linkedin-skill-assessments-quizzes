## Cybersecurity Assessment

#### Q1. Which of the three methods will copy the directory named "photo dir" recursively from the user's home directory to /backups?

```bash
cp -R "~/photo dir" /backups #method1
cp -R ~"/photo dir" /backups #method2
cp -R ~/"photo dir" /backups #method3
```

- [ ] None of the three methods will expand to the user's home directory. Only using `"$HOME/photo dir"`will be successful.
- [ ] Only method 1 will expand `"~/"` to the user's home directory and then append the quoted directory name that includes a space.
- [ ] Only method 2 will expand `"~/"` to the user's home directory and then append the quoted directory name that includes a space.
- [x] Only method 3 will expand `"~/"` to the user's home directory and then append the quoted directory name that includes a space.
