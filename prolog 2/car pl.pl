% owns(jack, Car1), (sedan(Car1) -> sedan(Car2); truck(Car1) -> truck(Car2)), owns(Who, Car2). %
owns(jack, car(bmw)).
owns(john, car(chevy)).
owns(olivia, car(civic)).
owns(jane, car(chevy)).

sedan(car(bmw)).
sedan(car(civic)).
truck(car(chevy)).

