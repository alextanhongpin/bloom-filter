# bloom-filter
Bloom filter implementation in various languages


## Use Cases
- approximately guess if email already exists from millions of existing emails.
- Malicious url detection. Rather than caching all the possible urls, we can use bloom filter instead.
- Medium uses bloom filter to avoid showing duplicate recommendations. The same can be used for tinder swipes suggestions.
- One hit wonders. Akamai and Facebook uses bloom filters to avoid caching items that are rarely searched or searched only once. Only when they are searched more than once, they are cached. So for each query, check if the item exists in the bloom filter already, if yes, and it’s not yet available in the cache yet, cache it.
- Unique identification system. Generate unique ids if it does not exist in the filter.
- Url shortener. Check for uniqueness of the urls.
- Financial fraud detection. We can add the blacklisted user in the list.
- the blacklist feature can also be useful to prevent users from entering blackllisted passwords.
- Facebook and linked in uses bloom filter for their typeahead search.
- ensure once only delivery, with a 1 percent chance of not delivering.
- unique counter. If the item does not exist in the bloom filter, increment the counter and add the item to the bloom filter.
- write code example for each of them.

## References

- https://stackoverflow.com/questions/4282375/what-is-the-advantage-to-using-bloom-filters
- https://www.quora.com/What-are-the-best-applications-of-Bloom-filters
- https://engineering.linkedin.com/open-source/cleo-open-source-technology-behind-linkedins-typeahead-search
