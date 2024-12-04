import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Sets a new value in Redis.
 * @param {string} schoolName - The key to set in Redis.
 * @param {string} value - The value to associate with the key.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

/**
 * Displays the value of a key from Redis.
 * @param {string} schoolName - The key to retrieve the value for.
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
    } else {
      console.log(reply);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
