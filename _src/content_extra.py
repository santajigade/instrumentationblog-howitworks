# Extra reading content for the first 12 pages: intro paragraphs, where it is used, field tips.
# Rules: max 2 sentences per paragraph, no hyphens in text, U+2212 for minus.
EXTRA = {}

EXTRA["orifice-plate"] = dict(
    intro=["The orifice plate is the oldest and still one of the most common flow elements in process plants. It is used on water, steam, natural gas and hydrocarbons because it is cheap, simple and calculated from a published standard.",
           "The plate itself does not measure anything. It creates a pressure difference, and a DP transmitter across two taps converts that difference into a flow signal.",
           "Because flow follows the square root of DP, the signal is strong at high flow and weak at low flow. That is why orifice loops are usually designed for normal flow between about 30 % and 90 % of the maximum."],
    uses=[("Steam flow", "Boiler outlet and header steam flow, often with pressure and temperature compensation."), ("Natural gas", "Fuel gas to furnaces and boilers, and many older custody meters."),
          ("Cooling and process water", "Large lines where a magmeter would be expensive."), ("Restriction orifices", "Plates that limit flow or drop pressure without measuring it.")],
    tips=["Install the plate with the sharp square edge facing upstream; a reversed plate reads low.", "Check that both impulse lines are full of liquid (or drained for gas) and at the same temperature.",
          "A worn or dented edge makes the meter read low; inspect plates during shutdowns.", "Keep the recommended straight run, or fit a flow conditioner, to avoid profile errors."])

EXTRA["magnetic-flow-meter"] = dict(
    intro=["Magnetic flow meters are the standard choice for water, wastewater, slurries and most water based chemicals. They have no obstruction in the pipe, so pressure loss is almost zero and solids pass straight through.",
           "The meter measures velocity, not mass, and it only works on liquids that conduct electricity. Accuracy of about 0.2 % to 0.5 % of reading is typical for a well installed meter.",
           "Most problems with magmeters come from installation rather than the sensor: poor grounding, a partly empty pipe or electrodes coated with deposits."],
    uses=[("Water and wastewater", "Raw water, treated water, sludge and effluent lines."), ("Slurries and pulp", "Mining slurries and paper stock, using abrasion resistant liners."),
          ("Chemical dosing", "Acids, alkalis and other conductive chemicals with PTFE or PFA liners."), ("Food and beverage", "Milk, juice and beer with hygienic connections.")],
    tips=["Mount the meter where the pipe is always full, such as a vertical pipe with upward flow.", "Use grounding rings or a grounding electrode on plastic or lined pipes.",
          "Keep the electrodes in the horizontal plane so air bubbles at the top do not touch them.", "If the reading is noisy, check conductivity, grounding and nearby VFD cables first."])

EXTRA["vortex-flow-meter"] = dict(
    intro=["Vortex flow meters count the vortices that form behind a bluff body, much like a flag flapping behind a pole. Because they have no moving parts, they are popular for steam, gases and clean liquids.",
           "The output is a frequency that is proportional to velocity over a wide range, often 10:1 or more. Many vortex meters add temperature and pressure sensors to give mass flow of steam or gas directly.",
           "The weak points are low flow, where vortices stop forming cleanly, and pipe vibration, which can look like flow to the sensor."],
    uses=[("Saturated and superheated steam", "Steam distribution and boiler output metering."), ("Compressed air and gases", "Air, nitrogen and process gas consumption."),
          ("Clean liquids", "Water, condensate and light hydrocarbons."), ("Utility metering", "Energy and cost allocation between plant areas.")],
    tips=["Size the meter for velocity, not pipe size; a smaller meter often gives better low flow performance.", "Avoid mounting near pumps, control valves or other vibration sources.",
          "Keep gaskets centred; a gasket protruding into the bore disturbs the vortex street.", "Set the low flow cutoff above the point where the signal becomes unstable."])

EXTRA["coriolis-flow-meter"] = dict(
    intro=["A Coriolis meter is the most direct way to measure mass flow. It also measures density and temperature, so one instrument can replace a flow meter, a densitometer and a temperature sensor.",
           "Accuracy of 0.1 % of reading or better on liquids makes Coriolis meters a common choice for custody transfer, batching and expensive products.",
           "The trade offs are price, weight in large sizes and sensitivity to entrained gas, which upsets the tube vibration."],
    uses=[("Custody transfer", "Crude oil, refined products and LPG loading."), ("Batching and dosing", "Accurate addition of ingredients and additives."),
          ("Density and concentration", "Product quality and blend control using the density output."), ("Difficult fluids", "Viscous, non Newtonian or multi component liquids.")],
    tips=["Do a zero adjustment at process conditions with the meter full and flow stopped.", "Avoid trapping gas: install so the tubes drain or fill completely depending on the fluid.",
          "Support the pipe on both sides but do not let the meter carry pipe stress.", "Watch drive gain; a sudden rise usually means gas, coating or a two phase problem."])

EXTRA["ultrasonic-flow-meter"] = dict(
    intro=["Transit time ultrasonic flow meters measure flow by timing sound pulses, so they have nothing in the flow path. Inline versions are used for custody transfer of gas and liquids; clamp on versions are popular for checks and retrofits.",
           "The time difference they measure is tiny, often a few hundred nanoseconds, so the electronics are very precise. Multi path meters average several sound paths to handle uneven flow profiles.",
           "For clean liquids and gases they work very well; heavy bubbles or solids scatter the sound and can stop the measurement."],
    uses=[("Water distribution", "Large pipelines where clamp on meters avoid cutting the pipe."), ("Natural gas custody", "Multi path gas ultrasonic meters at metering stations."),
          ("HVAC and energy", "Chilled and hot water flow for energy metering."), ("Temporary surveys", "Portable clamp on meters to check other flow meters.")],
    tips=["For clamp on meters, enter the exact pipe OD, wall thickness and material.", "Mount transducers on the side of horizontal pipes, not the top or bottom.",
          "Use fresh coupling gel or pads; poor coupling is a common cause of signal loss.", "Check the signal strength and sound speed readings as quick health diagnostics."])

EXTRA["turbine-flow-meter"] = dict(
    intro=["A turbine flow meter is a small propeller in the pipe that spins faster as flow increases. On clean, low viscosity liquids it gives excellent repeatability, which is why it is widely used for fuel and chemical batching.",
           "The meter produces pulses, and each pulse represents a fixed volume set by the K factor. This makes totalising and batching very simple.",
           "Because it has bearings and a moving rotor, a turbine meter needs clean fluid and occasional checks for wear."],
    uses=[("Fuel and oil metering", "Diesel, jet fuel and lube oil transfer."), ("Batching", "Filling and dosing with pulse totalisers."),
          ("Water and chemicals", "Clean water and low viscosity chemicals."), ("Test benches", "Reference meters for calibration rigs.")],
    tips=["Fit a strainer upstream to protect the rotor and bearings.", "Keep the meter full; air or vapour makes the rotor overspeed and damages bearings.",
          "Recheck the K factor if viscosity or temperature changes a lot.", "Do not exceed the maximum flow rating; overspeed shortens bearing life quickly."])

EXTRA["dp-level-measurement"] = dict(
    intro=["DP level measurement is the most widely used continuous level method in process plants. It works by measuring the hydrostatic pressure of the liquid column, which is simple, reliable and easy to verify.",
           "The key thing to remember is that the transmitter measures pressure, not height. The level is only correct if the liquid density is the one used for calibration.",
           "For closed or pressurised tanks, the low side is connected to the vapour space so the tank pressure cancels out."],
    uses=[("Storage tanks", "Water, chemical and fuel tanks, open or closed."), ("Boiler drums", "Drum level with density compensation for steam conditions."),
          ("Process vessels", "Separators, reactors and columns."), ("Interface and density", "Two transmitters can give density or interface level.")],
    tips=["Recalculate the range if the product density changes.", "For closed tanks, keep wet legs full or use dry legs that drain any condensate.",
          "Use remote seals for viscous, corrosive or crystallising liquids.", "Check zero with the tank empty or by equalising the manifold."])

EXTRA["radar-level-transmitter"] = dict(
    intro=["Radar level transmitters measure the time a microwave signal takes to reach the liquid surface and return. Because nothing touches the liquid, they suit corrosive, hot, sticky and hazardous products.",
           "Modern 80 GHz radars have a narrow beam that avoids most tank internals. The transmitter builds an echo curve and picks the true surface echo from it.",
           "Low dielectric liquids reflect only a small part of the signal, and foam or condensation on the antenna can weaken the echo further."],
    uses=[("Storage and process tanks", "Chemicals, fuels and water."), ("Solids silos", "Cement, grain and plastic pellets with suitable radars."),
          ("High temperature and pressure", "Reactors and columns where contact sensors struggle."), ("Inventory and tank gauging", "High accuracy radars for stock control.")],
    tips=["Mount away from the tank wall, inlet streams and agitator blades.", "Use false echo mapping with the tank as empty as possible.",
          "Keep the nozzle short or use an antenna that extends past the nozzle.", "For low dielectric products consider guided wave radar or a stilling well."])

EXTRA["displacer-level-transmitter"] = dict(
    intro=["Displacer level transmitters measure level by weighing a long cylinder hanging in the liquid. As the level rises, buoyancy reduces the apparent weight, and the transmitter turns that change into a level signal.",
           "They have been used for decades on separators, scrubbers and boiler drums, and they are still common for interface level between oil and water.",
           "Because the signal depends on density, the transmitter must be calibrated for the actual liquid or liquids in service."],
    uses=[("Oil and water separators", "Interface level between two liquids."), ("Knock out drums and scrubbers", "Level in high pressure gas service."),
          ("Feedwater heaters and drums", "Level in hot, high pressure vessels."), ("Replacement checks", "Reference for guided wave radar upgrades.")],
    tips=["Calibrate with weights or water, then correct for the real liquid density.", "Keep the cage vents and drains clear so the cage level matches the vessel.",
          "Check the torque tube for corrosion and the displacer for leaks or deposits.", "Lock the displacer before removing the head to avoid damaging the torque tube."])

EXTRA["bourdon-tube-pressure-gauge"] = dict(
    intro=["The Bourdon tube gauge is the most common local pressure gauge in the world. It needs no power, is easy to read and covers ranges from below 1 bar to over 1000 bar.",
           "Inside, a flattened curved tube straightens slightly under pressure, and a small gear movement turns that motion into a pointer reading.",
           "Most gauge failures come from overpressure, pulsation and vibration, which is why snubbers, liquid filling and correct range selection matter."],
    uses=[("Pumps and compressors", "Suction and discharge pressure at the machine."), ("Pipelines and headers", "Local check gauges next to transmitters."),
          ("Hydraulic systems", "High pressure circuits with liquid filled gauges."), ("Utilities", "Air, water, steam and gas services.")],
    tips=["Choose a range about twice the normal working pressure.", "Use a siphon on steam lines so hot steam never reaches the tube.",
          "Fit a snubber or liquid filled gauge where pressure pulsates.", "Replace gauges that do not return to zero after pressure is removed."])

EXTRA["thermocouple"] = dict(
    intro=["Thermocouples are the most widely used temperature sensors in industry. They are simple, rugged, cover very high temperatures and need no power at the sensor.",
           "The voltage they produce is small, about 41 µV per °C for type K, and it depends on the temperature difference between the hot and cold junctions. Correct extension cable and cold junction compensation are therefore essential.",
           "Accuracy is usually ± 1.5 °C to ± 2.5 °C at moderate temperatures, so RTDs are preferred where better accuracy is needed below about 600 °C."],
    uses=[("Furnaces and heaters", "Process heaters, boilers and heat treatment."), ("Exhaust and flue gas", "Engines, turbines and stacks."),
          ("Reactors and kilns", "High temperature chemical and cement processes."), ("Bearings and windings", "Machine protection with small, fast sensors.")],
    tips=["Use the correct extension or compensating cable all the way to the transmitter.", "Check polarity: reversing the wires makes the reading move the wrong way.",
          "Use a head mounted transmitter to keep the small mV signal away from noise.", "Replace thermocouples that have drifted after long use at high temperature."])

EXTRA["valve-positioner"] = dict(
    intro=["A valve positioner makes a control valve go exactly where the controller asks. Without it, friction in the packing and forces from the process can leave the valve several percent away from the requested position.",
           "Modern smart positioners use a microprocessor, a travel sensor and a fast pneumatic relay. They auto calibrate, report diagnostics over HART and can store valve signatures.",
           "Good positioner performance depends on clean dry air, a well set feedback linkage and sensible tuning."],
    uses=[("Control valves", "Flow, pressure, level and temperature control loops."), ("Split range control", "One signal driving two valves over different ranges."),
          ("Large actuators", "Fast stroking with volume boosters."), ("Valve diagnostics", "Partial stroke and signature tests with smart positioners.")],
    tips=["Run auto calibration after mounting or changing the linkage.", "Check supply pressure and air quality before blaming the positioner.",
          "Watch for hunting: reduce gain or check for high friction and stiction.", "Verify the fail position by removing the signal and the air supply."])
