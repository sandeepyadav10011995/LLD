## Dependency Inversion and Dependency Injection

  Dependency inversion and dependency injection are two concepts used in computer programming to make software more modular and easier to maintain.

    Dependency Inversion means that instead of a module (or piece of code) depending on other modules directly, it should depend on an abstraction 
    or interface. This makes the code more flexible because the module can work with different implementations of the abstraction.

    Dependency Injection is a technique to achieve dependency inversion. It means that instead of creating objects inside a module, you pass them in
    as arguments or set them as properties. This makes the code more testable and easier to change in the future.

So, in simple terms, dependency inversion is a concept that says we should depend on abstractions, not implementations. Dependency injection is a technique that helps us achieve dependency 
inversion by passing objects into code instead of creating them inside the code.

## Example -:
Let's say we have a class called Car that depends on a class called Engine. The Engine class contains the code for starting and stopping the car. 
Here's an example of how we might implement this without dependency inversion and dependency injection:

    class Engine:
        def start(self):
            # code for starting the engine

        def stop(self):
            # code for stopping the engine

    class Car:
        def __init__(self):
            self.engine = Engine()

        def start(self):
            self.engine.start()

        def stop(self):
            self.engine.stop()

In this example, the Car class depends directly on the Engine class. This violates the principle of dependency inversion because the Car class is coupled to 
the Engine class.

Now, let's see how we can apply dependency inversion and dependency injection to make this code more flexible and modular.

    from abc import ABC, abstractmethod

    class EngineInterface(ABC):
        @abstractmethod
        def start(self):
            pass

        @abstractmethod
        def stop(self):
            pass

    class Engine(EngineInterface):
        def start(self):
            # code for starting the engine

        def stop(self):
            # code for stopping the engine

    class Car:
        def __init__(self, engine: EngineInterface):
            self.engine = engine

        def start(self):
            self.engine.start()

        def stop(self):
            self.engine.stop()
In this example, we define an interface EngineInterface that the Engine class implements. The Car class now depends on the EngineInterface abstraction, 
rather than the Engine implementation directly.

We can now use dependency injection to pass in any object that implements the EngineInterface interface. For example, if we wanted to use a different 
engine in our Car class, we could create a new class that implements the EngineInterface interface, and pass it into the Car constructor:

    class DieselEngine(EngineInterface):
        def start(self):
            # code for starting a diesel engine

        def stop(self):
            # code for stopping a diesel engine

    diesel_engine = DieselEngine()
    car_with_diesel_engine = Car(diesel_engine)
In summary, dependency inversion is a principle that suggests we should depend on abstractions, not implementations. Dependency injection is a technique 
that helps us achieve dependency inversion by passing objects into code instead of creating them inside the code.





