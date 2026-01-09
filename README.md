# XOR Verifier Sandbox

**Purpose**: Test repository for XOR ability verification system.

> **WARNING**: This repository contains INTENTIONAL security issues for testing. Do not use this code in production.

## Contents

### Vulnerable Dependencies (ABILITY-001 testing)
- `requirements.txt` contains outdated packages with known CVEs

### Unpinned/Overprivileged Workflows (ABILITY-003 testing)
- `.github/workflows/unpinned.yml` - Actions without SHA pinning
- `.github/workflows/overprivileged.yml` - Overly broad permissions

### Risky Code (ABILITY-004 testing)
- `src/risky_code.py` - Code with security smells (eval, shell injection, etc.)
- `src/clean_code.py` - Control: well-written secure code

## Usage

This repo is used by XOR's ability verification CI:
1. Integration tests create PRs in this repo
2. Abilities run against those PRs
3. Tests verify abilities produce expected outputs
4. PRs are cleaned up automatically

## Do Not

- Use any code from this repo in production
- Manually create PRs (they may be auto-closed)
- Modify without updating corresponding test cases in `xor` repo
