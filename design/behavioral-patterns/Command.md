The command pattern is used to turn commands (or actions) into objects so that we can use these object to invoke that command, queue it, undo it, and do all kinds of things with it.
It means that the command object should have all the information required to perform the said command.
This makes the object independent and portable, meaning every client can easily execute it.

This pattern is comprised of:
- A receiver - the class that the action is performed on.
- A base command  - abstract class or interface.
- Concrete commands - actual actions.
- An executor - the class that executes the command (can be done by the client or by a dedicated class)

Let's take an example of a drive plan for a car.
We have a `Car` which can turn right or left, it can go, and it can stop.
```
enum Direction {
  Left,
  Right,
}

class Car {
  private stopped: boolean = true;

  turn(direction: Direction): void {
    if (this.stopped) {
      console.log("Can't turn while stopped");
    } else {
      console.log(`Turning ${Direction[direction]}`);
    }
  }

  stop(): void {
    if (this.stopped) {
      console.log('Already stopped');
    } else {
      this.stopped = true;
      console.log('Stopping');
    }
  }

  go(): void {
    if (!this.stopped) {
      console.log('Already going');
    } else {
      this.stopped = false;
      console.log('Going...');
    }
  }
}
```

Did you guess what's the car's role in this example?

Of course you did! 
It's the **receiver**.
Why is it the receiver?
Because it is the object on which the actual action happens.

### Base Command
The base command in our example is an abstract class (could also be an interface).
It should hold all the information required to perform the command, in our case, it should hole the car instance on which to perform the action.
It also has an `execute()` method that performs the command.
```
abstract class Command {
  protected car: Car;

  constructor(car: Car) {
    this.car = car;
  }

  abstract execute(): void;
}
```
### Concrete commands
Our concrete commands implement the actions executed on the `Car`.
```
class TurnLeftCommand extends Command {
  constructor(car: Car) {
    super(car);
  }

  execute(): void {
    this.car.turn(Direction.Left);
  }
}
```
We also have `TurnRightCommand`, `GoCommand`, and `StopCommand`.

### Executor
Our executor is the class `PathExecutor` that has a queue of commands.
We can add commands to the queue, and we can execute the entire queue.
```
class PathExecutor {
  private commands: Command[] = [];

  queueCommand(command: Command): void {
    this.commands.push(command);
  }

  executeAll(): void {
    for (const command of this.commands) {
      command.execute();
    }
  }
}
```

### Client Code
Here is an example of using this pattern.
```
const myCar: Car = new Car();
const pathExecutor: PathExecutor = new PathExecutor();
pathExecutor.queueCommand(new GoCommand(myCar));
pathExecutor.queueCommand(new TurnRightCommand(myCar));
pathExecutor.queueCommand(new TurnRightCommand(myCar));
pathExecutor.queueCommand(new TurnLeftCommand(myCar));
pathExecutor.queueCommand(new StopCommand(myCar));
pathExecutor.executeAll();
```

### Summary
The command pattern allows us to turn actions into object thus enabling other classes to execute these command at different times.
It also encapsulates the inner workings of the command and hides it from the client.
Another important benefit of this pattern is the ease of extensibility, to add another command one simply needs to create a new class that extends `Command` and the existing code will immediately support it.
### JavaScript
Possible JavaScript code for this pattern:
```
class Car {
  constructor() {
    this.stopped = true;
  }

  turn(direction) {
    if (this.stopped) {
      console.log("Can't turn while stopped");
    } else {
      console.log(`Turning ${direction}`);
    }
  }

  stop() {
    if (this.stopped) {
      console.log('Already stopped');
    } else {
      this.stopped = true;
      console.log('Stopping');
    }
  }

  go() {
    if (!this.stopped) {
      console.log('Already going');
    } else {
      this.stopped = false;
      console.log('Going...');
    }
  }
}

class Command {
  constructor(car) {
    this.car = car;
  }

  execute() {}
}

class TurnLeftCommand extends Command {
  constructor(car) {
    super(car);
  }

  execute() {
    this.car.turn('Left');
  }
}

class TurnRightCommand extends Command {
  constructor(car) {
    super(car);
  }

  execute() {
    this.car.turn('Right');
  }
}

class GoCommand extends Command {
  constructor(car) {
    super(car);
  }

  execute() {
    this.car.go();
  }
}

class StopCommand extends Command {
  constructor(car) {
    super(car);
  }

  execute() {
    this.car.stop();
  }
}

class PathExecutor {
  constructor() {
    this.commands = [];
  }

  queueCommand(command) {
    this.commands.push(command);
  }

  executeAll() {
    for (const command of this.commands) {
      command.execute();
    }
  }
}

const myCar = new Car();
const pathExecutor = new PathExecutor();
pathExecutor.queueCommand(new GoCommand(myCar));
pathExecutor.queueCommand(new TurnRightCommand(myCar));
pathExecutor.queueCommand(new TurnRightCommand(myCar));
pathExecutor.queueCommand(new TurnLeftCommand(myCar));
pathExecutor.queueCommand(new StopCommand(myCar));
pathExecutor.executeAll();

```