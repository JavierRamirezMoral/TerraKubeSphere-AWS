
console.log('Loading event');
var AWS = require('aws-sdk');
var dynamodb = new AWS.DynamoDB({apiVersion: '2012-08-10'});
var tableName = "RegisterChatbot_Registrations";

// Close dialog with the customer, reporting fulfillmentState of Failed or Fulfilled
function close(sessionAttributes, fulfillmentState, message) {
    return {
        sessionAttributes,
        dialogAction: {
            type: 'Close',
            fulfillmentState,
            message,
        },
    };
}

function storeRegistration(intent, callback) {

    let userInfo = {};

    // store every slot we received as part of registration
    Object.keys(intent.currentIntent.slots).forEach((item) => {
        console.log(item)
        userInfo[item] = {"S": intent.currentIntent.slots[item]};
    });

    // store a registration date
    userInfo.registration_date = {"S": new Date().getTime().toString() };
    userInfo.registration_userid = {"S": intent.userId};
    
    dynamodb.putItem({
        "TableName": tableName,
        "Item" : userInfo
    }, function(err, data) {
        if (err) {
            console.log('Failure storing user info');
            console.log(err);
            callback(close(intent.sessionAttributes, 'Fulfilled',
            {'contentType': 'PlainText', 'content': "I am sorry, but something went wrong saving your Registration Info. Please try again."}));
        } else {
            console.log("Successfully Stored UserInfo");
            callback(close(intent.sessionAttributes, 'Fulfilled',
            {'contentType': 'PlainText', 'content': "Thank you for registering for our service."}));
        }
    });
}

// --------------- Main handler -----------------------
 
// Route the incoming request based on intent.
// The JSON body of the request is provided in the event slot.
exports.handler = (event, context, callback) => {
    console.log(event);
    try {
        storeRegistration(event,
            (response) => {
                callback(null, response);
            });
    } catch (err) {
        callback(err);
    }
};