// Include the BV-BRC JavaScript client library
const BVBRCClient = require('bvbrc_js_client');

// Instantiate the service with the API endpoint
const svc = new BVBRCClient("https://patricbrc.org/api");

// Initialize the service with endpoint and token (optional)
svc.init(endpoint, token);

// Example usage of base API methods
(async () => {
    try {
        // Get schema for a data type
        const schema = await svc.getSchema('genome');
        console.log('Schema:', schema);

        // Get a single item of a data type (genome in this case)
        const genome = await svc.get('genome', '227377.26');
        console.log('Genome:', genome);

        // Query for data using RQL syntax
        const queryResult = await svc.query('genome', 'eq(genome_id,227377.26)');
        console.log('Query Result:', queryResult);
    } catch (error) {
        console.error('Error:', error);
    }
})();
