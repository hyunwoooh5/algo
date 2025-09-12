SELECT firstName, lastName, city, state FROM Person
LEFT JOIN address
    on Person.personID = address.personID