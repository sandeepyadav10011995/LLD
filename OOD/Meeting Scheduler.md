
**Problem**
A **meeting scheduler** software allows organizations to schedule and book meetings for a group of participants. The scheduler determines a meeting time and location depending on the availability of the participants. It ensures that most of the intended participants can effectively meet on the specified date and interval. The system allows users to book and cancel meetings. The invited participants promptly receive these notifications. The organizer can also add new participants to a meeting after the meeting is scheduled.

**Expectations** 
	1. Room Assignments
		i. How does the system determine available rooms?
		ii. How important is the capacity of a room when assigning  a room for a meeting?
	2. Availability Of Attendees
		i. How does the system check the availability of the attendees?
		ii. How does the system access the meeting information of all the attenedees?

**Components**
	1. Interval
	2. Meeting Room
	3. Meeting
	4. Calender

**Design Pattern**
The design pattern used to design the meeting scheduler-:
	* Singleton Design Pattern

**Requirements**
	R1: There should be an n number of meeting rooms.
	R2: Each meeting room should have a specific capacity to accomodate the desired number of people.
	R3: If not reserved already, each meeting room should have the ability to be booked along with setting an interval (start time, end time) for the meeting.
	R4: A notification needs to be sent to all the people invited to the meeting.
	R5: Users will receive an  invite regardless of whether they are available at the intereval or not. User can respond to the invitation by accepting or rejecting the invite.

**Diff elements of the meeting scheduler system -:**
1. System -: Meeting Schduler
2. Actors
	1. Primary Actors
		1. Scheduler -: Schedule and cancel meetings and book and release meeting rooms.
		2. User -: Accept and Reject invitations and will decide their presence for the meetings
	2. Secondary Actors
		1. System -: Sends out the notifications regarding any new meetings or cancellations.

**Use Cases**
1. Scheduler
	1. Schedule/Cancel meeting
	2. Book/Release room
2. User
	1. Attend meeting
	2. Accept/Reject meeting
3. System
	1. Send invite notification
	2. Send cancelation notification

**Components Of Meeting Scheduler**
	1. User
		- name: String
		- email: String
		+ respondInvitation(invite): None/Void	
	 2. Interval
		- startTime: date/time
		 - endTime: date/time
	3. Meeting Room
		 - id: int
		 - capacity: int
		 - bookedIntervals: list[Interval]
		 - isAvailable: bool
	4. Meeting
		 - id: int
		 - participants: list[User]
		 - interval: Interval
		 - room: MeetingRoom
		 - subject: String
		 + addParticipants(participants: list): None
	5. Calender
		 - meetings: list[Meeting]
	6. Meeting Scheduler
		 - organizer: User
		 - calender: Calender
		 - rooms: list[Meeting Room]
		 + scheduleMeeting(users: list[User], interval: Interval): bool
		 + cancelMeeting(users: list[User], interval): bool
		 + bookRoom(room, numberOfPersons, interval): bool
		 + releaseRoom(room, interval): bool
		 + checkRoomsAvailability(numberOfPersons, interval): MeetingRoom
	7. Notification
		 - notificationId: int
		 - content: String
		 - creationDate: date/time
		 + sendInvite(user): None
		 + cancelNotification(user): None



**CODE**

User.py
```
 class User: 
	def __init__(self, name, email): 
		self.__name = name 
		self.__email = email 
		
	 def respond_invitation(self, invite): 
		 pass

```

Interval.py
```
class Interval: 
	def __init__(self, start_time, end_time): 
		self.__start_time = start_time 
		self.__end_time = end_time
		
```

MeetingRoom.py
```
class MeetingRoom: 
	def __init__(self, id, capacity, is_available): 
		self.__id = id 
		self.__capacity = capacity 
		self.__is_available =     is_available 
		self.__booked_intervals = []
```

Calender.py
```
class Calendar: def __init__(self): 
	self.__meetings = []
```

Meeting.py
```
class Meeting: 
	def __init__(self, id, participants_count, interval, room, subject): 
		self.__id = id self.__participants_count = participants_count
		self.__participants = [] 
		self.__interval = interval self.__room = room 
		self.__subject = subject 
	def add_participants(self, participants): 
		pass
```

Meeting Scheduler.py
```
class __MeetingScheduler(object): 
	__instances = None # Scheduler is a singleton class that ensures it will have only one active instance at a time 
	def __new__(cls): 
		if cls.__instances is None: 
		cls.__instances = super(__MeetingScheduler, cls).__new__(cls) 
		return cls.__instances 
class MeetingScheduler(metaclass=__MeetingScheduler): 
	def __init__(self, organizer, calendar): 
		self.__organizer = organizer 
		self.__calendar = calendar 
		self.__rooms = [] 
	def schedule_meeting(self, users, interval): 
		pass 
	def cancel_meeting(self, users, interval): 
		pass 
	def book_room(self, room, number_of_persons, interval): 
		pass 
	def release_room(self, room, interval): 
		pass 
	def check_rooms_availability(self, number_of_persons, interval): 
		pass
```

Notification.py

```
class Notification: 
	def __init__(self, notification_id, content, creation_date):
		self.__notification_id = notification_id 
		self.__content = content 
		self.__creation_date = creation_date 
	def send_notification(self, user): 
		pass 
	def cancel_notification(self, user): 
		pass
```

