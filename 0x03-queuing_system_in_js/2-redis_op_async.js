import { createClient, print } from 'redis';
import { promisify } from 'util';
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const getAsync = promisify(client.get).bind(client);

/**
 * Sets a new value in Redis.
 * @param {string} schoolName - The key to set in Redis.
 * @param {string} value - The value to associate with the key.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

/**
 * Displays the value of a key from Redis using async/await.
 * @param {string} schoolName - The key to retrieve the value for.
 */
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
  }
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
