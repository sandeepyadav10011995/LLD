  ridersController.book(r1, 0.0, 0.0, 500.0, 500.0);
    ridersController.book(r2, 0.0, 0.0, 500.0, 500.0);

    System.out.println("\n### Printing current trips for r1 and r2");
    System.out.println(ridersController.fetchHistory(r1).getBody());
    System.out.println(ridersController.fetchHistory(r2).getBody());

    cabsController.updateCabLocation(c5, 50.0, 50.0);

    System.out.println("\n### Printing current trips for r1 and r2");
    System.out.println(ridersController.fetchHistory(r1).getBody());
    System.out.println(ridersController.fetchHistory(r2).getBody());

    cabsController.endTrip(c5);

    System.out.println("\n### Printing current trips for r1 and r2");
    System.out.println(ridersController.fetchHistory(r1).getBody());
    System.out.println(ridersController.fetchHistory(r2).getBody());


    assertThrows(NoCabsAvailableException.class, () -> {
      ridersController.book(r3, 0.0, 0.0, 500.0, 500.0);
    });

    ridersController.book(r4, 48.0, 48.0, 500.0, 500.0);
    System.out.println("\n### Printing current trips for r1, r2 and r4");
    System.out.println(ridersController.fetchHistory(r1).getBody());
    System.out.println(ridersController.fetchHistory(r2).getBody());
    System.out.println(ridersController.fetchHistory(r4).getBody());

    assertThrows(RiderNotFoundException.class, () -> {
      ridersController.book("abcd", 0.0, 0.0, 500.0, 500.0);
    });

    assertThrows(RiderAlreadyExistsException.class, () -> {
      ridersController.registerRider("r1", "shjgf");
    });

    assertThrows(CabAlreadyExistsException.class, () -> {
      cabsController.regiserCab("c1", "skjhsfkj");
    });

    assertThrows(CabNotFoundException.class, () -> {
      cabsController.updateCabLocation("shss", 110.0, 110.0);
    });

    assertThrows(CabNotFoundException.class, () -> {
      cabsController.updateCabAvailability("shss", false);
    });
