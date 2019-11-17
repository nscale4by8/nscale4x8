# nscale4x8
This repository contains information and resources related to my N Scale layout started 2019.

## Prototype Inspiration

I am loosely modeling the Cleveland Flats from around 1960. I selected the prototype location for the opportunity to model densely packed industries and a complex web of rails. The prototype includes grades with over and under passes, level crossings, and multiple lift bridges.

![Turnout at Lift Bridge](prototypeInspiration/turnoutAtLiftBridge.png)

- [B&O Right of Way Crossing Over Flats Industrial RR Right of Way](prototypeInspiration/BandO_overFlatsIndustrial.png)
- [Lift Bridges Over and Under](prototypeInspiration/LIftBridgesOverUnder.png)
- [Curved Approach to Lift Bridge](prototypeInspiration/curveToLiftBridge.png)
- [Crossing at Approach to Bridge](prototypeInspiration/levelCrossingAtBridge.png)
- [Multiple Spurs to Industries with MAny Grade Level Crossings](prototypeInspiration/industry.png)

## Track Plan

The plan is inspired by the famous [Atlas Granite Gorge & Northern](https://www.modeltrainforum.com/picture.php?albumid=241&pictureid=2492). I adapted it to enable more continuous run variations. 

- The adapted plan can be configured as a double track figure eight with two trains running in opposite directions.
- The adapted plan enables local switching operations on sidings while other trains run continuously.
- The adapted plan can be configured as a twisted dog-bone that crosses the river six times before traveling over the same segment of rail twice.
- The adapted plan provides two variants of out-and-back originating either direction from the industries along the river.
  
![Plan](plan/rev8s.png)

[Plan](../blob/master/benchwork/Rev8Blocks.pdf)

## 3D Printed Custom Bridges

![Models and Prototype Inspirations](Custom3DPrintedModels.png)
[Models](Custom3DPrintedBridges.md)

## Benchwork, Test Fit, and Controls

The benchwork is currently dry-fit. Nothing is glued down. All of the wiring is in place for four separate electrical blocks. All turnouts are remotely operated by the Control System. I plan to test the layout for a while to assure reliable operation because once the benchwork is glued, it will be very difficult to modify wiring.

The benchwork consists of 1x2 dimensional lumber covered with 2 inch medium density foam. Then another quarter inch of foam covers everywhere except the river. Channels are cut in the quarter inch foam to provide routing for bundles of wires. On top of the quarter inch later, one inch foam "feet" support the lowest track elevations. Feet of various lengths create grades and elevated sections. Pre-primed Masonite rests atop the foam feet. Track will eventually be glued to the Masonite.

![Benchwork](benchwork/IMG_0104.png)

![Benchwork](benchwork/IMG_0110.png)

[Benchwork](benchwork/benchwork.md)

## Electronic Control

Layout control is implemented by a Raspberry Pi B+ with an add-on "hat" that provides four motor controllers. Three motor controllers are used as throttles so that three separate trains can be independently controlled. The remaining motor controller is connected through relays to actuate remote turnouts (one turnout at a time). Sixteen relays are individually controlled using general purpose input/output pins provided by the Raspberry Pi.

The Raspberry Pi provides wireless access accepting commands from a laptop or smart phone. Each throttle can be manually set, and each turnout can be actuated independently. However, there are three pre-configured fully automated "modes" that may be selected. Once selected, all of the turnouts are set appropriately for the mode, and throttles are adjusted under computer control. This allows a quick setup for passive operation to watch trains run. I may take the layout to a show sometime, and full computer control will be useful in that environment. I'll be able to chat or even walk away from the layout while it runs itself.

![Control](controls/IMG_0125.png)

[Control](controls/Control.md)
