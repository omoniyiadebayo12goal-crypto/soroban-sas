import re

with open('src/client.rs', 'r') as f:
    content = f.read()

# Replace assert_eq!(client.fetch_admin(&rpc).unwrap(), expected_admin);
content = content.replace(
    'assert_eq!(client.fetch_admin(&rpc).unwrap(), expected_admin);',
    'assert_eq!(client.fetch_admin(&rpc).unwrap().to_string(), expected_admin.to_string());'
)

# Replace assert_eq!(client.get_attestation(&rpc, &uid).unwrap(), Some(expected));
content = content.replace(
    'assert_eq!(client.get_attestation(&rpc, &uid).unwrap(), Some(expected));',
    'assert_eq!(client.get_attestation(&rpc, &uid).unwrap().map(|a| a.to_xdr(a.uid.0.env())), Some(expected).map(|a| a.to_xdr(a.uid.0.env())));'
)

# Replace assert_eq!(client.get_attestations_by_attester(&rpc, &attester.to_string()).unwrap(), expected);
content = content.replace(
    'assert_eq!(client.get_attestations_by_attester(&rpc, &attester.to_string()).unwrap(), expected);',
    'let fetched = client.get_attestations_by_attester(&rpc, &attester.to_string()).unwrap();\n        let fetched_xdr: Vec<_> = fetched.iter().map(|u| u.0.to_array()).collect();\n        let expected_xdr: Vec<_> = expected.iter().map(|u| u.0.to_array()).collect();\n        assert_eq!(fetched_xdr, expected_xdr);'
)

# Replace assert_eq!(client.fetch_attester_key(&rpc, &attester.to_string()).unwrap(), Some(expected));
content = content.replace(
    'assert_eq!(client.fetch_attester_key(&rpc, &attester.to_string()).unwrap(), Some(expected));',
    'assert_eq!(client.fetch_attester_key(&rpc, &attester.to_string()).unwrap().map(|k| k.to_xdr(k.key.env())), Some(expected).map(|k| k.to_xdr(k.key.env())));'
)

# Replace in paginated_indexer_queries_decode_a_page_from_simulation
content = content.replace(
    'assert_eq!(page.items, vec![expected_uid]);',
    'let items_arrays: Vec<_> = page.items.iter().map(|u| u.0.to_array()).collect();\n        assert_eq!(items_arrays, vec![expected_uid.0.to_array()]);'
)

# Fix fetch_schema_existing_missing_and_round_trip
content = content.replace(
    'assert_eq!(client.fetch_schema(&rpc, registry_contract_id, &uid).unwrap(), Some(expected_record.clone()));',
    'assert_eq!(client.fetch_schema(&rpc, registry_contract_id, &uid).unwrap().map(|s| s.to_xdr(s.uid.0.env())), Some(expected_record.clone()).map(|s| s.to_xdr(s.uid.0.env())));'
)

# Fix fetch_schema_by_content_round_trip_and_missing
content = content.replace(
    'assert_eq!(client.fetch_schema_by_content(&rpc, registry_contract_id, "foo", &resolver, true).unwrap(), Some(expected_record));',
    'assert_eq!(client.fetch_schema_by_content(&rpc, registry_contract_id, "foo", &resolver, true).unwrap().map(|s| s.to_xdr(s.uid.0.env())), Some(expected_record).map(|s| s.to_xdr(s.uid.0.env())));'
)

# Fix compute_schema_uid_matches_common_derivation
content = content.replace(
    'assert_eq!(client_uid, expected_uid);',
    'assert_eq!(client_uid.0.to_array(), expected_uid.0.to_array());'
)

with open('src/client.rs', 'w') as f:
    f.write(content)

