# AC51002 Coursework 1

## DundeeZest Conveyor Belt System

**Overview**  
DundeeZest is a company providing affordable luxury wear for University of Dundee students. They are planning to upgrade their production line by implementing a conveyor belt system to improve efficiency.

### **System Operation**

- **Operating Hours:** The conveyor belt system will run every day from **9 AM to 5 PM**.
- **Start Requirement:** Production requires an operator's input to initiate each day.

### **Production & Maintenance Requirements**

- **Production Rate:** The system will produce a predetermined number of items per hour.
- **Maintenance Schedule:** Routine maintenance is required after a specified number of operating hours.
- **Service Notification:** Once the operating hours reach the maintenance threshold, the system will:
  - Display a “Service Required” message.
  - Show the **total number of items produced** since the last maintenance.
  - Shut down until maintenance is completed.

### **Maintenance Cycle**

- After completing maintenance, all production data will reset, and the production-maintenance cycle will restart.

**Objective**  
DundeeZest has tasked you with developing a **prototype Python software system** that manages the maintenance component of the conveyor belt system, ensuring it receives regular servicing to prevent breakdowns.

### Requirement List

1. It should allow an operator to start production for each day by typing in an input. You can decide
   what this input will be. The input cannot change and operation for the day cannot commence
   without it. [X]
2. Once operation commences, the software will continue to monitor production until the daily
   limit of operating hours is reached i.e. 9am – 5pm. Assume 1 hour to be equivalent to a single
   count by the Python interpreter e.g. a count from 1 to 2 makes 1 hour.[X]
3. It should be able to store the total operating hours in a .txt file and retrieve the value at the start
   of the next day’s operation. [X]
4. At the end of each day, it should update the total operating hours and store the updated value
   in the .txt file in requirement 3 above. [X]
5. Include in the software a set value for the number of items that can be produced in an hour (e.g.,
   100 items/hour). This could be a fixed value. [X]
6. The software should be able to store the total number of items produced either in the .txt file in
   requirement 3 above or a separate file and retrieve the value at the start of the next day’s
   operation. [X]
7. It should be able to record the total number of items produced, in the appropriate file and
   update the value at the end of each day. [X]
8. It should display a 'Service Required' message when the maximum limit of operating hours is
   reached (a value can be assumed for this). It should also display the total number of items
   produced since the last maintenance.
9. It should reset all production and operational data, including total items produced and
   operating hours, to prepare for the next production cycle. It is assumed that the routine
   maintenance has been completed at this point.
   Task A: Write a Python program that meets the above requirements for the conveyor belt system.
   Task B: Briefly describe each variable and function you have used in one sentence. The descriptions can
   be included as comments in your program.
   Task C: Requirements 10 and 11 are optional. Attempting them means you can get additional marks, but
   only proceed with them if you have successfully completed the main requirements above.
10. Assume that the conveyor belt will be used by 4 operators and only one of them operates it per
    day. Your software should keep track of the number of items produced by each operator and
    display their individual totals at the point of maintenance along with the other data in
    requirement 8 above.
11. Update requirement 8 above so that the information is displayed for exactly 10 seconds before
    the system shuts down for maintenance.

**Task A**: Write a Python program that meets the above requirements for the conveyor belt system.
**Task B**: Briefly describe each variable and function you have used in one sentence. The descriptions can
be included as comments in your program.
**Task C**: Requirements 10 and 11 are optional. Attempting them means you can get additional marks - only start these after requirements 1-9 are done
