# Security Assumptions
- Soroban auth is used to verify signers.
- Expirations are checked against ledger timestamps.
- Off-chain attestation signatures are domain-separated: the signed digest
  commits to the network id, the verifying contract address, and a nonce, so
  signatures cannot be replayed across networks, contracts, or nonces
  (see [offchain-attestations.md](offchain-attestations.md)).
- The ed25519 public key presented with an off-chain attestation must be the
  key of the declared attester account; this is enforced by comparing it
  against the attester address's XDR encoding.
