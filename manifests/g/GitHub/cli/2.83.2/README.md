GitHub CLI (gh) winget manifests — v2.83.2

Files provided:
- GitHub.cli.yaml (version manifest)
- GitHub.cli.installer.yaml (installer manifest)
- GitHub.cli.locale.en-US.yaml (locale manifest)

Installer SHA256s (verified):
- x64: 4D296C785AFA586F75B505A6B7B875F17F727A97EB85589771D8B18E6AE541C8
- x86: 7D0C7AE7AEC849DE43D9A241EDB474095AD0C6AF2E51FE881C943F2199BAD357

Notes:
- The installer URLs point to the official GitHub Releases page for gh v2.83.2.
- SHAs were computed by downloading the official MSIs and verifying them.

How to test locally:
```powershell
winget create --manifest manifests\g\GitHub\cli\2.83.2\GitHub.cli.installer.yaml
```

Replace or update manifests as needed before publishing.