# TollGate - Prior Work Documentation

This repository serves as documentation for approaches that have already been tried when building TollGate. It helps new contributors understand TollGate's current state and learn from previously encountered challenges.

## Setting up your nsite

To get started with TollGate, you'll need to set up your nsite configuration. Use the `nsite-cli` command to begin the setup process:

```bash
$ nsite-cli
```

The setup wizard will guide you through the following steps:

1. Enter your NOSTR private key (or press Enter to create a new one)
2. Provide your website or project name
3. Add a project description
4. Configure your Blossom server URLs (default: https://nostr.download)

### Example Setup Output
```bash
nsite:config Project file not found at .nsite/project.json +0ms
nsite-cli: No existing project configuration found. Setting up a new one:
✔ 1. Existing NOSTR private key (nsec/hex) (Enter to create a NEW one): 
✔ 2. Web site or project name: ...
✔ 3. Web site or project description: ...
? 5. Blossom server URLs: https://nostr.download
? 5. Blossom server URLs: Done.
nsite:config Project configuration saved to .nsite/project.json +41s
```

### Available Commands

Once configured, you can use the following commands:

- `upload <folder>`: Upload files from a directory
- `ls [npub]`: List all files available online
- `download <targetfolder> <npub>`: Download all files available online

For help with any command, use the `-h` or `--help` option.

## Contributing

We welcome contributions to this documentation! If you've tried an approach that isn't documented here, please feel free to add it.

