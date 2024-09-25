### Example of creature config:

```jsonc
"uglyVampire" :
{
	"name": {
		"plural": "Ugly Vampire",
		"singular": "Ugly Vampires"
	},
	"faction": "necropolis",
	"doubleWide": false,
	"advMapAmount": {
		"max": 8,
		"min": 3
	},
	"attack": 8,
	"defense" : 10,
	"damage": {
		"max": 12,
		"min": 6
	},
	"level": 4,
	"growth": 4,
	"hitPoints": 40,
	"speed": 6,
	"shots": 0, // Will be ignored if creature does not shoot
	"aiValue": 400,
	"abilities" : {},
	"upgrades": ["core:vampireLord"],
	"graphics" :
	{
		"animation": "CVAMP.DEF"
	},
	"sound" :
	{
		"attack": "VAMPATTK.wav",
		"defend": "VAMPDFND.wav",
		"killed": "VAMPKILL.wav",
		"move": "VAMPMOVE.wav",
		"wince": "VAMPWNCE.wav",
		"startMoving": "VAMPEXT1.wav",
		"endMoving": "VAMPEXT2.wav"
	}
}
```

#### Example of creatur ebailities using Bonus system:

```jsonc
"abilities":
{
	"castDisease" : // Ability id (any)
	{
		"type" : "SPELL_AFTER_ATTACK",
		"subtype" : "spell.disease",
		"val" : 20 // Chance, in percent
	},
		"drainsLife" : // Another ability id
	{
		"type" : "LIFE_DRAIN",
		"val" : 100 //Percent of life drained
	}
}
```

### Example of offensive spell with projectile animation and extra effect:

```jsonc
"magicBolt" : {
	"index" : 16,
	"targetType": "CREATURE",

	"name": "Magic Bolt",
	"school": {
		"air": false,
		"earth": true,
		"fire": false,
		"water": false
	},

	"animation":{
		"projectile": [
			{"minimumAngle": 0 ,"defName":"C08SPW4"},
			{"minimumAngle": 0.60 ,"defName":"C08SPW3"},
			{"minimumAngle": 0.90 ,"defName":"C08SPW2"},
			{"minimumAngle": 1.20 ,"defName":"C08SPW1"},
			{"minimumAngle": 1.50 ,"defName":"C08SPW0"}
		],
		"hit":["C08SPW5"]
	},
	"sounds": {
		"cast": "ICERAY"
	},
	"levels" : {
		"base":{
			"range" : "0",
			"battleEffects" : {
				"directDamage" : {"type":"core:damage"}
			},
			"targetModifier":{"smart":true}
		}
	},
	"flags" : {
		"damage": true,
		"offensive": true,
		"negative": true
	},
	"targetCondition": {
		"allOf": {},
		"anyOf": {},
		"noneOf": {
			"core:bonus.DIRECT_DAMAGE_IMMUNITY": "normal",
			"core:bonus.NON_LIVING": "normal",
			"core:bonus.UNDEAD": "normal"
		}
	},
	"levels": { // Configuration for every Water Magic secondary skill level
		"base": {
			"aiValue": 5,
			"range": "0",
			"targetModifier": {
				"smart": true
			}
		},
		"none": {
			"description": "{Magic Bolt}\n\nDoes little damage to target and reduces its speed for this turn.\n",
			"cost": 8,
			"power": 10,
			"effects": {
				"speed": {
					"type": "STACKS_SPEED",
					"valueType": "PERCENT_TO_ALL",
					"duration": "STACK_GETS_TURN",
					"val": -25
				}
			}
		},
		"basic": {
			"description": "{Basic Magic Bolt}\n\nDoes little damage to target and reduces its speed for this turn.\n",
			"cost": 6,
			"power": 15,
			"effects": {
				"speed": {
					"type": "STACKS_SPEED",
					"valueType": "PERCENT_TO_ALL",
					"duration": "STACK_GETS_TURN",
					"val": -25
				}
			}
		},
		"advanced": {
			"description": "{Advanced Magic Bolt}\n\nDoes little damage to target and reduces its speed for this turn.\n",
			"cost": 6,
			"power": 15,
			"effects": {
				"speed": {
					"type": "STACKS_SPEED",
					"valueType": "PERCENT_TO_ALL",
					"duration": "STACK_GETS_TURN",
					"val": -50
				}
			}
		},
		"expert": {
			"description": "{Expert Magic Bolt}\n\nDoes little damage to target and reduces its speed for this turn.\n",
			"cost": 6,
			"power": 15,
			"effects": {
				"speed": {
					"type": "STACKS_SPEED",
					"valueType": "PERCENT_TO_ALL",
					"duration": "STACK_GETS_TURN",
					"val": -75
				}
			}
		}
	}
}
```

### Example of combined artifact:

```jsonc
"barbarianLordsAxeOfFerocity": {
	"type": [
		"HERO"
	],
	"slot": "RIGHT_HAND",
	"class": "RELIC",
	"value": 16000,
	"components": [
		"ogresClubOfHavoc",
		"targOfTheRampagingOgre",
		"crownOfTheSupremeMagi",
		"tunicOfTheCyclopsKing"
	],
	"bonuses": [
		{
			"type": "ADDITIONAL_ATTACK",
			"val": 1,
			"valueType": "BASE_NUMBER",
			"limiters": [
				"noneOf",
				"SHOOTER_ONLY"
			]
		}
	],
	"graphics": {
		"image": "artifacts/HrArt158",
		"large": "artifacts/HrArt158L",
		"map": "artifacts/zart158.def"
	},
	"text": {
		"name": "Barbarian Lord's Axe of Ferocity",
		"description": "{Barbarian Lord's Axe of Ferocity}\r\n\r\nWhen worn, grants an additional strike each round to all non-shooting creatures in a hero's army.",
		"event": "You pick up the Barbarian Lord's Axe of Ferocity and it speaks to your mind - Bring on the enemy and together we shall cut a swath of destruction through their legions!"
	}
}
```

### Example of small random map template:

```jsonc
{
	"2SM2a" :
	{
		"minSize" : "s", "maxSize" : "s+u", //s - small, u - with underground
		"players" : "2",
		"zones" :
		{
			"1" :
			{
				"type" : "playerStart",
				"size" : 11,
				"owner" : 1,
				"monsters" : "normal",
				"playerTowns" : { "castles" : 1 },
				"mines" : { "wood" : 1, "ore" : 1 },
				"treasure" :
				[
					{ "min" : 10000, "max" : 15000, "density" : 1 },
					{ "min" : 3000, "max" : 6000, "density" : 6 },
					{ "min" : 500, "max" : 3000, "density" : 9 }
				]
			},
			"2" :
			{
				"type" : "playerStart",
				"size" : 11,
				"owner" : 2,
				"monsters" : "normal",
				"playerTowns" : { "castles" : 1 },
				"minesLikeZone" : 1,
				"treasureLikeZone" : 1
			},
			"3" :
			{
				"type" : "treasure",
				"size" : 11,
				"monsters" : "normal",
				"neutralTowns" : { "towns" : 1 },
				"matchTerrainToTown" : false,
				"mines" : { "mercury" : 1, "sulfur" : 1, "gold" : 1 },
				"treasure" :
				[
					{ "min" : 15000, "max" : 20000, "density" : 1 },
					{ "min" : 10000, "max" : 15000, "density" : 6 },
					{ "min" : 3000, "max" : 6000, "density" : 9 }
				]
			},
			"4" :
			{
				"type" : "treasure",
				"size" : 11,
				"monsters" : "normal",
				"neutralTowns" : { "towns" : 1 },
				"matchTerrainToTown" : false,
				"mines" : { "crystal" : 1, "gems" : 1, "gold" : 1 },
				"treasureLikeZone" : 3
			}
		},
		"connections" :
		[
			{ "a" : "1", "b" : "3", "guard" : 3000 },
			{ "a" : "2", "b" : "4", "guard" : 3000 },
			{ "a" : "1", "b" : "4", "guard" : 12500 },
			{ "a" : "2", "b" : "3", "guard" : 12500 }
		]
	}
}
```

### Example of custom terrain:

```jsonc
"stardust": {
	"text": "Stardust",
	"moveCost": 100,
	"minimapUnblocked": [ //RGB color of passable terrain
		131,
		86,
		172
	],
	"minimapBlocked": [ //RGB color of blocked terrain
		104,
		61,
		174
	],
	"music": "stardust/Stardust Theme",
	"tiles": "stardust/startTerrian",
	"river": "starRiver",
	"rockTerrain": "rock",
	"shortIdentifier": "sd",
	"type": [
		"SUB", // Can spawn underground
		"SURFACE"
	],
	"battleFields": [
		"stardust"
	],
	"horseSound": "horse07",
	"horseSoundPenalty": "horse27"
}
```

### Example hero configuration:

```jsonc
"tarnumBarbarian":
{
	"class": "barbarian",
	"female": false,
	"special": false,
	"texts": {
		"name": "Tarnum",
		"biography": "Tarnum is a young Barbarian who has spent his entire life under the oppression of the Wizard-Kings of Bracaduun, but he's always dreamed that life could be better - should be better.",
		"specialty": {
			"description": "{Offence}\r\n\r\nReceives a 5% per level bonus to Offense skill percentage.",
			"tooltip": "Skill bonus: Offense.",
			"name": "Offence"
		}
	},
	"images": {
		"specialtySmall": "Tarnum/Barbarian/spec-small.bmp",
		"specialtyLarge": "Tarnum/Barbarian/spec-large.bmp",
		"large": "Tarnum/Barbarian/portrait-large.bmp",
		"small": "Tarnum/Barbarian/portrait-small.bmp"
	},
	"army": [
		{
			"creature": "goblin",
			"max": 25,
			"min": 15
		},
		{
			"creature": "goblinWolfRider",
			"max": 7,
			"min": 5
		},
		{
			"creature": "orc",
			"max": 6,
			"min": 4
		}
	],
	"skills": [
		{
			"level": "advanced",
			"skill": "offence"
		}
	],
	"specialty": {
		"bonuses": {
			"offence": {
				"subtype": 0,
				"targetSourceType": "SECONDARY_SKILL",
				"type": "PERCENTAGE_DAMAGE_BOOST",
				"val": 5,
				"valueType": "PERCENT_TO_BASE",
				"updater": "TIMES_HERO_LEVEL"
			}
		}
	}
}
```

### Example of hero class:

```jsonc
"aristocrat":
{
	"affinity": "might", // or "magic"
	"animation": {
		"battle": {
			"female": "courtyard/heroes/battleFemaleLord",
			"male": "courtyard/heroes/battleMaleLord"
		}
	},
	"commander": "courtCommander",
	"defaultTavern": 5,
	"faction": "courtyard",
	"lowLevelChance": {
		"attack": 45,
		"defence": 30,
		"knowledge": 10,
		"spellpower": 15
	},
	"highLevelChance": {
		"attack": 30,
		"defence": 25,
		"knowledge": 20,
		"spellpower": 25
	},
	"mapObject": {
		"templates": {
			"default": {
				"animation": "courtyard/heroes/CourtFemaleMightMap"
			}
		}
	},
	"name": "Aristocrat",
	"primarySkills": {
		"attack": 2,
		"defence": 1,
		"knowledge": 1,
		"spellpower": 2
	},
	"secondarySkills": { //Weighted chance to gain
		"airMagic": 3,
		"archery": 4,
		"armorer": 3,
		"artillery": 5,
		"ballistics": 5,
		"diplomacy": 7,
		"eagleEye": 1,
		"earthMagic": 1,
		"estates": 8,
		"fireMagic": 3,
		"intelligence": 1,
		"leadership": 6,
		"learning": 4,
		"logistics": 7,
		"luck": 4,
		"mysticism": 1,
		"navigation": 5,
		"necromancy": 0,
		"offence": 4,
		"pathfinding": 5,
		"resistance": 5,
		"scholar": 1,
		"scouting": 2,
		"sorcery": 2,
		"tactics": 3,
		"waterMagic": 2,
		"wisdom": 4,
		"firstAid": 1
	},
	"tavern": { // Weighted chance to appear in tavern
		"castle": 7,
		"conflux": 5,
		"courtyard": 8,
		"dungeon": 5,
		"fortress": 2,
		"inferno": 6,
		"necropolis": 4,
		"rampart": 3,
		"stronghold": 4,
		"tower": 6
	}
}
```

### Example of new secondary skill:

```jsonc
"hexes":
{
	"name": "Hexes",
	"gainChance": {
		"might": 4,
		"magic": 6
	},
	"base": {
		"effects": {
			"main": {
				"type": "LUCK",
				"propagator": "BATTLE_WIDE",
				"propagationUpdater": "BONUS_OWNER_UPDATER",
				"limiters": [
					"OPPOSITE_SIDE"
				],
				"val": -1
			}
		}
	},
	"basic": {
		"images": {
			"small": "skills/hexes/hexesSmallBasic",
			"medium": "skills/hexes/hexesMediumBasic",
			"large": "skills/hexes/hexesLargeBasic"
		},
		"description": "{Basic Hexes}\n\nReduces opponent's Luck by 1.",
		"effects": {
			"main": {
				"val": -1
			}
		}
	},
	"advanced": {
		"images": {
			"small": "skills/hexes/HexesSmallAdvanced",
			"medium": "skills/hexes/HexesMediumAdvanced",
			"large": "skills/hexes/HexesLargeAdvanced"
		},
		"description": "{Advanced Hexes}\n\nReduces opponent's Luck by 2.",
		"effects": {
			"main": {
				"val": -2
			}
		}
	},
	"expert": {
		"images": {
			"small": "skills/hexes/HexesSmallExpert",
			"medium": "skills/hexes/HexesMediumExpert",
			"large": "skills/hexes/HexesLargeExpert"
		},
		"description": "{Expert Hexes}\n\nReduces opponent's Luck by 3.",
		"effects": {
			"main": {
				"val": -3
			}
		}
	}
}
```

### Example of configurable object with custom reward:

```jsonc
"airMagicMushroom":
{
	"name": "Air Magic Mushroom",
	"handler": "configurable",
	"types": {
		"airMagicMushroom": {
			"name": "Magic Air Mushroom (grant expert Air Magic until end of the week)",
			"onVisitedMessage": "{Magic Air Mushroom}\r\n\r\nYou already visited this mushroom this week.",
			"visitMode": "bonus",
			"rmg": {
				"value": 2000,
				"rarity": 20,
				"zoneLimit": 1
			},
			"sounds": {
				"ambient": [
					"LOOPFAER"
				],
				"visit": [
					"LUCK"
				]
			},
			"rewards": [
				{
					"bonuses": [
						{
							"type": "MAGIC_SCHOOL_SKILL",
							"subtype": "spellSchool.air",
							"val": 3,
							"duration": "ONE_WEEK"
						}
					],
					"message": "{Magic Air Mushroom}\r\n\r\nThe influence of this mysterious mushroom allows you to cast Air Magic spells at expert level until the end of the week."
				}
			],
			"templates": {
				"zobj012": {
					"animation": "mapObjects/zobj012.def",
					"mask": [
						"VVV",
						"VVV",
						"VAV"
					],
					"visitableFrom": [
						"---",
						"+++",
						"+++"
					]
				}
			}
		}
	}
}
```

### Example of custom creature bank:

```jsonc
"core:creatureBank": {
	"types": {
		"churchyard": {
			"resetDuration": 4, // Reset and make revisitable after 4 days
			"rmg": {
				"zoneLimit": 2,
				"mapLimit" : 10,
				"value": 1500, //Determines strength of a guard
				"rarity": 100
			},
			"levels": [
				{
					"chance": 70, //Chances must sum up to 100
					"guards": [
						{
							"amount": 8,
							"type": "halfling"
						},
						{
							"amount": 8,
							"type": "halfling"
						},
						{
							"amount": 80,
							"type": "peasant"
						},
						{
							"amount": 80,
							"type": "peasant"
						},
						{
							"amount": 80,
							"type": "peasant"
						},
						{
							"amount": 8,
							"type": "halfling"
						}
					],
					"reward": {
						"value": 3000,
						"resources": {
							"gold": 800
						},
						"creatures": [
							{
								"amount": 4,
								"type": "walkingDead",
								"upgradeChance": 50
							}
						],
						"artifacts": [
							{
								"class": "MINOR"
							}
						]
					}
				},
				{
					"chance": 30,
					"guards": [
						{
							"amount": 15,
							"type": "halfling"
						},
						{
							"amount": 15,
							"type": "halfling"
						},
						{
							"amount": 150,
							"type": "peasant"
						},
						{
							"amount": 150,
							"type": "peasant"
						},
						{
							"amount": 150,
							"type": "peasant"
						},
						{
							"amount": 15,
							"type": "halfling"
						}
					],
					"reward": {
						"value": 12000,
						"resources": {
							"gold": 1500
						},
						"creatures": [
							{
								"amount": 8,
								"type": "walkingDead",
								"upgradeChance": 50
							}
						],
						"artifacts": [
							{
								"class": "MINOR"
							}
						]
					}
				}
			]
		}
	}
}
```

### Example of a custom biome:

```jsonc
{
	"forestRuins" : {
		"biome":{
			"terrain" : [ "dirt","grass","swamp" ],
			"alignment" : "neutral",
			"objectType" : "structure"
		},
		"templates" : ["NHRns01", "NHRns02", "NHRns03", "NHRns04", "NHRns05", "NHRns06", "NHRns07", "NHRns08"]
	}
}
```