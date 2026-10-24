# SAS Prometheus Metrics Exporter

A Prometheus metrics exporter for Soroban SAS (Stellar Attestation Service) events.

## Overview

This tool provides a Prometheus metrics endpoint for monitoring SAS contract activity. It exposes metrics for the event types defined in the `soroban-sas-sdk`.

## Metrics

### Counters

- `sas_attestation_issued_total` - Total number of attestations issued
- `sas_attestation_revoked_total` - Total number of attestations revoked
- `sas_batch_attested_total` - Total number of batch attestations completed
- `sas_batch_revoked_total` - Total number of batch revocations completed
- `sas_schema_registered_total` - Total number of schemas registered
- `sas_fee_config_updated_total` - Total number of fee configuration updates
- `sas_indexer_strict_updated_total` - Total number of indexer strict policy updates

### Gauges

- `sas_active_attestations` - Current number of active attestations
- `sas_active_schemas` - Current number of active schemas

### Histograms

- `sas_event_processing_duration_seconds` - Duration of event processing in seconds

## Usage

### Build

```bash
cargo build -p soroban-sas-prometheus-exporter
```

### Run

```bash
# Set required environment variable
export SAS_CONTRACT_ID="C..."

# Run the exporter
./target/debug/soroban-sas-prometheus-exporter
```

### Environment Variables

- `SAS_CONTRACT_ID` - SAS contract ID to monitor (required)
- `SCHEMA_REGISTRY_CONTRACT_ID` - Schema Registry contract ID to monitor (optional)
- `INDEXER_CONTRACT_ID` - Indexer contract ID to monitor (optional)
- `METRICS_ADDR` - Prometheus metrics server address (default: `0.0.0.0:9090`)

### Accessing Metrics

Once running, metrics are available at `http://localhost:9090/metrics`:

```bash
curl http://localhost:9090/metrics
```

## Prometheus Configuration

Add the following to your `prometheus.yml`:

```yaml
scrape_configs:
  - job_name: 'soroban-sas'
    static_configs:
      - targets: ['localhost:9090']
    scrape_interval: 15s
```

## Example Queries

### Rate of attestations issued per hour
```
rate(sas_attestation_issued_total[1h])
```

### Active attestations over time
```
sas_active_attestations
```

### Recent schema registrations
```
rate(sas_schema_registered_total[5m])
```

## Architecture

The exporter:
1. Exposes Prometheus metrics via an HTTP endpoint on `/metrics`
2. Metrics are updated when events are recorded using the `record_event` method
3. The gauge metrics (`active_attestations`, `active_schemas`) are maintained by incrementing on creation events and decrementing on revocation events

Note: This is a metrics-only exporter. Event polling from the Soroban RPC is not implemented in the current version. The metrics are designed to be updated by an external event processor that calls `record_event` with parsed SAS events.

## Development

### Run tests

```bash
cargo test -p soroban-sas-prometheus-exporter
```

### Run with debug logging

```bash
RUST_LOG=debug cargo run -p soroban-sas-prometheus-exporter
```

## License

Same as the parent soroban-sas project.
