import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from '../8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    const [job1, job2] = queue.testMode.jobs;

    expect(job1.type).to.equal('push_notification_code_3');
    expect(job1.data).to.eql(jobs[0]);
    expect(job2.type).to.equal('push_notification_code_3');
    expect(job2.data).to.eql(jobs[1]);
  });

  it('should log job creation and completion', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
    ];

    const log = [];
    const consoleLog = console.log;
    console.log = (msg) => log.push(msg);

    createPushNotificationsJobs(jobs, queue);

    queue.testMode.jobs[0].emit('complete');

    expect(log).to.include(`Notification job created: ${queue.testMode.jobs[0].id}`);
    expect(log).to.include(`Notification job ${queue.testMode.jobs[0].id} completed`);

    console.log = consoleLog;
  });

  it('should log job failure', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
    ];

    const log = [];
    const consoleLog = console.log;
    console.log = (msg) => log.push(msg);

    createPushNotificationsJobs(jobs, queue);

    queue.testMode.jobs[0].emit('failed', new Error('Something went wrong'));

    expect(log).to.include(`Notification job ${queue.testMode.jobs[0].id} failed: Error: Something went wrong`);

    console.log = consoleLog;
  });

  it('should log job progress', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
    ];

    const log = [];
    const consoleLog = console.log;
    console.log = (msg) => log.push(msg);

    createPushNotificationsJobs(jobs, queue);

    queue.testMode.jobs[0].emit('progress', 50);

    expect(log).to.include(`Notification job ${queue.testMode.jobs[0].id} 50% complete`);

    console.log = consoleLog;
  });
});
