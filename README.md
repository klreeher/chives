
an archive for the fediverse.

## built on

## federation

chives supports [activity pub](),

## Spec Profiles

1. client to server -- the Social API
2. server to server -- the Federation API

Client
	Implements the client portion of the Federation protocol
Server
	implements the server portion of the federation protocol
Federated Server
	implements both ends of the federation protocol

## HTTP Verbs

`POST` 
  creates only. throws dupe error if object already exists.
`PUT`
  creates or updates if the object referenced already exists
`DELETE`
>The Delete activity is used to delete an already existing object. The side effect of this is that the server MAY replace the object with a Tombstone of the object that will be displayed in activities which reference the deleted object. If the deleted object is requested the server SHOULD respond with either the HTTP 410 Gone status code if a Tombstone object is presented as the response body, otherwise respond with a HTTP 404 Not Found.




## data models

### Actors

Users:
	- have an outbox and inbox
	- can follow other users
	- can follow works
	- can like works  

```
{
  "@context": ["https://www.w3.org/ns/activitystreams",
               {"@language": "ja"}],
  "type": "User",
  "id": "https://kenzoishii.example.com/",
  "following": "https://kenzoishii.example.com/following.json",
  "followers": "https://kenzoishii.example.com/followers.json",
  "liked": activityStream URL/ID,
  "inbox": "https://kenzoishii.example.com/inbox.json",
  "outbox": "https://kenzoishii.example.com/feed.json",
  "preferredUsername": "kenzoishii",
  "name": "石井健蔵",
  "summary": "この方はただの例です",
  "icon": [
    "https://kenzoishii.example.com/image/165987aklre4"
  ]
}
```

todo:
- oauth properties

### Objects

#### Works

a work is created by a User. a work has a type, and provides creator information.
a work can be followed by a user, and added to collections.
works can be commented on

{
  "@context": ["https://www.w3.org/ns/activitystreams",
               {"@language": "en"}],
  "type": "Note",
  "id": "http://postparty.example/p/2415",
  "content": "<p>I <em>really</em> like strawberries!</p>",
  "source": {
    "content": [id_ch01, id_ch02],
    "mediaType": chapteredWork}
}

types:
- chaptered work
- multi-media work
- audio work
- video work
- image work
- rec list work

### Collections

- series: collection of works 
- chaptered work: a collection of works
- 