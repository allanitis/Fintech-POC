let Swagger = require('swagger-client');

exports.handler = function (event, context, callback) {

    callback(null, { "message": "Successfully executed" });
    Swagger.http({
        url: `https://api.exchangerate-api.com/v4/latest/USD`,
        method: 'get',
        query: {},
        headers: { "Accept": "application/json" }
    }).then((response) => {
        console.log(response.body.rates)
    }).catch((err) => {
        // error handling goes here
    });
}