Proxy is a structural design pattern that provides an object that acts as a substitute for a real service object used by a client.

Proxies can sometimes appear very similar to facades.
The key difference is that a proxy implements the interface that the proxied element implements.
Facade, on the other hand, wraps the element and adds other methods.

A simple example of proxy can be a bouncer in a club.
Let's say we have a `Club` interface that opens the door and accepts party people:
```
interface Club {
  openDoor(partyPerson: PartyPerson): void;
}
```
We have a `PublicClub` that implements it:
```
class PublicClub implements Club {
  openDoor(partyPerson: PartyPerson): void {
    console.log('Welcome!');
  }
}
```
Our proxy is a `ClubWithBouncer`:
```
class ClubWithBouncer implements Club {
  private publicClub: PublicClub = new PublicClub();

  openDoor(partyPerson: PartyPerson): void {
    if (partyPerson.getAge() >= 21) {
      this.publicClub.openDoor(partyPerson);
    } else {
      console.log('Not allowed');
    }
  }
}
```
This implementation of `Club` acts as a security proxy for `PublicClub`.
It will not allow people younger than 21 to enter.
This is a client example, first two party people try to enter a `PublicClub` and then the `ClubWithBouncer`
```
const tooYoung: PartyPerson = new PartyPerson(20);
const old: PartyPerson = new PartyPerson(30);
const publicClub: PublicClub = new PublicClub();
console.log('Public club:');
publicClub.openDoor(tooYoung);
publicClub.openDoor(old);
const clubWithBouncer: ClubWithBouncer = new ClubWithBouncer();
console.log('Club with bouncer:');
clubWithBouncer.openDoor(tooYoung);
clubWithBouncer.openDoor(old);
```
Output:
```
Public club:
Welcome!
Welcome!
Club with bouncer:
Not allowed
Welcome!
```

The proxy can be very useful in many situations: providing security, adding caching for heavy objects, and more.
Remember that for the client, a proxy can completely replace the "real" object, the client might not even know what the real object is.