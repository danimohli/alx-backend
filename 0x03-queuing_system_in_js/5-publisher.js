import { createClient } from 'redis';

// Create a Redis client
const publisher = createClient();

// Event: Connection successful
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});
publisher.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Publishes a message to a Redis channel after a delay.
 * @param {string} message - The message to publish.
 * @param {number} time - The delay in milliseconds before publishing.
 */
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

publishMessage('Hello, Holberton!', 100);
publishMessage('This is a test message.', 200);
publishMessage('KILL_SERVER', 300);
