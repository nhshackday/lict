#!/bin/bash

# /mnt/nhshackday/je4d/pubmed-scrape/xml/$i

echo ./drug_mapping.py /mnt/nhshackday/je4d/pubmed-scrape/xml/$1 ">" /mnt/nhshackday/je4d/pmcid-to-drug-id-$1
exec ./drug_mapping.py /mnt/nhshackday/je4d/pubmed-scrape/xml/$1 > /mnt/nhshackday/je4d/pmcid-to-drug-id-$1
