# Security and local configuration

This repository preserves an academic prototype. Use an isolated local database and synthetic media/accounts when reproducing it. Dependency versions reflect the historical environment; current service compatibility and a production deployment have not been certified.

Keep credentials in local environment files and use separate random secrets for user sessions and internal workers. Never publish bearer tokens, database dumps containing accounts, notebook outputs containing personal data, or service-account keys. Keep worker ports on loopback/private networking and configure the intended browser origin explicitly.

Any credential previously published must be revoked or rotated at its issuing service. Removing a literal from the current source does not revoke it or erase Git history. History filtering does not change credentials at their issuing services; exposed credentials still need to be revoked or rotated by their owner.

For private reporting, contact the repository owner through the contact details on their GitHub profile. Do not include live secrets in a public issue.
