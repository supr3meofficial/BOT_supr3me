import discord
from discord.ext import commands
import random
import asyncio

class CaseOpeningCog:

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.guild_only()
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def opencase(self, ctx, rigged_argument = "normal_drop_rate"):

			member = ctx.author

			#Case Opening Items

			case_items = [
			"M9 Bayonet | Doppler `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_knife_m9_bayonet_am_doppler_phase1_light_large.1a9960a6bba1a82aeab00b0207b4ff7c423a1f06.png",         #0
			"Karambit | Doppler `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_knife_karambit_am_doppler_phase1_light_large.16c0819028af598b772826c2bc675712a1d5af37.png",           #1
			"AK-47 | Bloodsport `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_ak47_gs_ak47_bloodsport_light_large.40f076f6b92e08acc37860923533aa9768795b2b.png",           #2
			"M4A1-S | Decimator `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_m4a1_silencer_gs_m4a1_decimator_light_large.5af82e99273fcc0a4ad35b2971b63787ee989d6a.png",           #3
			"AWP | Oni Taji `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_awp_cu_awp_hannya_light_large.ed3c0ec0e7ea85781983f7aba5d358c260c6749b.png",               #4
			"AWP | Hyper Beast `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_awp_cu_awp_hyper_beast_light_large.7dd26637e8d50bc129d25ebdbf3e6e410917808e.png",            #5
			"USP-S | Torque `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_usp_silencer_cu_usp_progressiv_light_large.91cde781cd0c8502bbbb66f37cc7f1baf2a10c05.png",               #6
			"AUG | Ricochet `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_aug_am_aug_jumble_light_large.d86901a42f239ddc39cd645d2a17281881fe37d5.png",               #7
			"Galil-AR | Rocket Pop `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_galilar_cu_galilar_particles_light_large.8732f64d53dbc9b0c732641655d4f99124d8cacc.png",        #8
			"MAG-7 | Sonar `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_mag7_am_mag7_malform_light_large.8a87c99550a4f609e7357bb4f63facf86279afca.png",                #9
			"UMP-45 | Riot `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_ump45_cu_ump45_uproar_light_large.04cd84320c4370bced14a3989b0e141cff67ec88.png",                #10
			"M4A1-S | Flashback `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_m4a1_silencer_cu_m4a1_flashback_light_large.5e6c2d582d33006425b61dc0e0e8c28ecda9f853.png",           #11
			"Desert Eagle | Crimson Web `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_hy_webs_darker_light_large.7b9cb19bac52ebe7c49e3abdfb0c400ea252fef8.png",   #12
			"Desert Eagle | Kumicho Dragon `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_aq_deserteagle_kumichodragon_light_large.19874e9a20cfac49efbe1f1557b995e453633ffe.png",#13
			"AK-47 | Case Hardened `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_ak47_aq_oiled_light_large.92c8d125e4e54758d37e946496030e9a18833b58.png",        #14
			"Bayonet | Case Hardened `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_bayonet_aq_oiled_light_large.920866e2a1f17fda7702e0b4cb95f45a8a8c0070.png",      #15
			"Bowie Knife | Tiger Tooth `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_knife_survival_bowie_an_tiger_orange_light_large.a8cf2f4214c950f59798f15d0013f7a33e6972fa.png",    #16
			"Bloodhound Gloves | Snakebite `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/studded_bloodhound_gloves_bloodhound_snakeskin_brass_light_large.7e478dfcfe8c89cf4f4651ee547bb1b0ed0f05f9.png",#17
			"PP-Bizon | Osiris `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_bizon_cu_bizon-osiris_light_large.269e03e1ad598b76adb884704c4f48d725beb5fc.png",            #18
			"M4A4 | Evil Daimyo `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_m4a1_cu_m4a4_evil_daimyo_light_large.c208ba252c0d8902caa973a634cbfa945508a716.png",           #19
			"Galil-AR | Crimson Tsunami `;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposbupIgthwczbYQJF7dC_mL-cluHxDLfYkWNF18lwmO7Eu9z03APi-hY-MW_1JIKXelc5ZgnW-FO2yevvgJLpvc7NzSE1uiMr4HbD30vg7rDTf40/360fx360f",   #20
			"P250 | Wingshot `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_p250_hy_p250_crackshot_light_large.538a33bb8d7af894f965257c39f699168e125cdd.png",              #21
			"Glock-18 | Bunsen Burner `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_glock_aq_glock18_flames_blue_light_large.5fed23d5a32793c25914eeb99b45f1a2b0cb9d6c.png",     #22
			"P2000 | Pulse `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_hkp2000_cu_p2000_pulse_light_large.a79fcfcd59202495573abfddc1e7627be62b4e1c.png",                #23
			"AK-47 | Elite Build `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_ak47_cu_ak47_mastery_light_large.4305c0ba4b02ce531fc08c275fa6a9d87da2cf7e.png",          #24
			"MP7 | Armor Core `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_mp7_aq_mp7_ultramodern_light_large.5351e1926e4a9599d149c4941a8603f4143ff999.png",             #25
			"MP7 | Urban Hazard `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_mp7_cu_mp7-commander_light_large.260d3f2765c83f75eadac5abd6ef4187ea2c2089.png",           #26
			"Five-SeveN | Urban Hazard `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_fiveseven_cu_fiveseven_urban_hazard_light_large.456966d23faf1034c51b8130b7a70294af087026.png",    #27
			"Sawed-Off | Origami `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_sawedoff_cu_sawedoff_origami_light_large.5f1b3cef6d518cda69daafddd9b2c240a29cf0cc.png",          #28
			"M249 | System Lock `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_m249_cu_m249_sektor_light_large.c957e70c656024b2c062f7af2031a76cb3c83f1c.png",           #29
			"Negev | Terrain `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_negev_sp_negev_turq_terrain_light_large.9c6c678b0e6bc949c0688f3e1cf39ca73e0a44ae.png",              #30
			"M9 Bayonet | Autotronic `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_knife_m9_bayonet_gs_m9_bay_autotronic_light_large.f81f68f78b0b40717602fc88f62b4d7af346c430.png",      #31
			"Shadow Daggers | Slaughter `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_knife_push_am_zebra_light_large.a09a6cf348b102f80e87226cc71d03544e502703.png",   #32
			"Flip Knife | Crimson Web `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_knife_flip_hy_webs_light_large.e0bcc9e1d004bff0af07abc34a609c6654835ce6.png",     #33
			"Driver Gloves | Convoy `;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DAX1R3LjtQurWzLhRfwP_BcjZ94dW6nZSKhe7LPr7Vn35c18lwmO7Eu92s2FW1-ko4NWjxJYGdegE-YA3U-wC_lbvmgMe_tcidzXdquikntH3D30vgtGG3lFU/360fx360f",       #34
			"Driver Gloves | Crimson Weave `;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DAX1R3LjtQurWzLhRfwP_BcjZ9_tmyq42Ok_7hPoTdl3lW7Ysn27jA8dyh2FLk-kQ-a276doTGIQY8aVvZ81Lql-u81pLqvcjMmCY1pGB8soKYr6Bu/360fx360f",#35
			"AK-47 | Fire Serpent `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_ak47_cu_fireserpent_ak47_bravo_light_large.9390e7fd091ea8a0434fd2143e0acf0d5d1bbc97.png",         #36
			"Desert Eagle | Golden Koi `;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposr-kLAtl7PLFTi5B7dCzh7-JhfbiPITdn2xZ_Pp9i_vG8MKji1a1_0VqamymI4LEelRrNFHT-ATvyO680Me-uMjIzXQw6HV04CragVXp1igFofN6/360fx360f",    #37
			"M4A1-S | Bright Water `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_m4a1_silencer_hy_ocean_bravo_light_large.7a942449926153575269af174733edc7bed5faeb.png",        #38
			"USP-S | Orion `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_usp_silencer_cu_usp_spitfire_light_large.883b877a8a57c9dd1128f2550ddd694d959f3150.png",                #39
			"M4A1-S | Atomic Alloy `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_m4a1_silencer_am_m4a1-s_alloy_orange_light_large.82bd272d0256f17eb86029a8d1411c4e5bf2bc9c.png",        #40
			"SCAR-20 | Cyrex `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_scar20_cu_scar_cyrex_light_large.ee4da13e2d74d0fd1fdbaa8f2ca49eb1c7f0acca.png",              #41
			"CZ75-Auto | Twist `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_cz75a_am_gyrate_light_large.90f97369a79695a7fdcb633a9c9a9e56f29a05d5.png",            #42
			"P2000 | Oceanic `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_hkp2000_hy_p2000_oceani_light_large.8f64654c5964975c85201b1dbbdf7b8ffab768be.png",                #43
			"Glock-18 | Off World `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_glock_cu_glock_indigo_light_large.3786c7c3be7d03ee053050af2f7a8427782742e1.png",         #44
			"UMP-45 | Metal Flowers `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_ump45_aq_ump45_flameflower_light_large.9c5aedb21ad6461f0761375c53b50f030fa0e10c.png",       #45
			"Tec-9 | Cut Out `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_tec9_aq_tec9_chalk_pattern_light_large.e0425d0a56ca5a2240b71495a5ef2bc4af0e9331.png",              #46
			"M4A4 | Neo-Noir `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_m4a1_cu_m4a4_neo_noir_light_large.b03bd6902c1d714af0bd4795dce8e653dd12dcc9.png",              #47
			"MP7 | Bloodsport `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_mp7_gs_mp7_bloodsport_light_large.ab5c304901ceb320482742b041815e7b5e3ccb95.png",             #48
			"AWP | Mortis `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_awp_gs_awp_death_light_large.19bdee04e6a0b4a3b8f832fd8ea18fea1e558f2e.png",                 #49
			"USP-S | Cortex `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_usp_silencer_cu_usp_cut_light_large.573fc8c594667e378f3ed9890ce48bbb586e8de0.png",               #50
			"AUG | Stymphalian `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_aug_gs_aug_stymphalian_birds_light_large.0840c45db138a07275c2250a0881fe752f27c601.png",            #51
			"Glock-18 | Moonrise `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_glock_aa_glock_18_urban_moon_fever_light_large.a0227f81e44dba68abbe595d427d62f9f90da99d.png",          #52
			"UMP-45 | Arctic Wolf `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_ump45_cu_ump45_white_fang_light_large.f63a10d5ee18e3045adfdcf963b9067b3b0a6b48.png",         #53
			"MAG-7 | SWAG-7 `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_mag7_aq_mag7_swag7_light_large.20341e396db88a5ecde84f8b803a500f4aec3b55.png",               #54
			"Negev | Lionfish `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_negev_sp_negev_lionfish_light_large.f8326a67617c5138ab8b6f6afc81375fbd091033.png",             #55
			"Nova | Wild Six `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_nova_gs_nova_anchorite_light_large.419b869b5316b67a6ed673edafd088a9d16c066c.png",              #56
			"R8 Revolver | Grip `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_revolver_gs_revolver_tread_light_large.7c3bd1302f62853e5694aec2d70cf1c7140b3fc0.png",           #57
			"P2000 | Urban Hazard `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_hkp2000_cu_p2000_urban_hazard_light_large.17657c4e9c3379f634c78e4d02ca9e9facbe9edb.png",         #58
			"Five-SeveN | Flame Test `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_fiveseven_gs_fiveseven_hot_rod_violet_light_large.66cb3d6336f4ea07a7f4ebbd3192c59f0afca3fc.png",      #59
			"SG 553 | Aloha `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_sg556_sp_sg533_aloha_light_large.03aa863680ab2223924ae9cbe8b7662a84fb162c.png",               #60
			"MP9 | Black Sand `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_mp9_cu_mp9_black_sand_light_large.37dce08f403ec73c1e16b3dc46068b22293e9514.png",             #61
			"PP-Bizon | Night Riot `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_bizon_cu_bizon_riot_light_large.2f0848b27a917287062306f49870cf9ec06bbbbe.png",        #62
			"XM1014 | Oxide Blaze `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_xm1014_cu_xm1014_oxide_blaze_light_large.691be80b706e1ea4faf9b5c9bec40b3611b1d440.png",         #63
			"Hydra Gloves | Case Hardened `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/studded_hydra_gloves_bloodhound_hydra_case_hardened_light_large.611be49c3a2f37057a7740c8ad74cc818f688b3d.png", #64
			"Hydra Gloves | Emerald `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/studded_hydra_gloves_bloodhound_hydra_black_green_light_large.16bbb88e6be97ca92f5227a59d3f76560fccaf80.png",       #65
			"Hydra Gloves | Rattler `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/studded_hydra_gloves_bloodhound_hydra_snakeskin_brass_light_large.953e703a64d078c26bf8075c3b5a8525d91ce74e.png",       #66
			"Hydra Gloves | Mangrove `;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DAR0hwIQFTibK8LxVh7PTEfitH_-O0mI-Ek__7JrXVqWNI7Ndwte7T8In7t1ixqgc0NiucedPWKmlsIwmTuT7jlLq2wMvT4MyLnid97iErsXaLnhW21BtIOuM8jP2XGlSfBKxLTaKHDyDZ5JwhHimsTRq0kn8QmKa57KE18Q/360fx360f",      #67
			"Specialist Gloves | Fade `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/specialist_gloves_specialist_fade_light_large.93080c3004ae36aa520d87fd0ceb04463298453c.png",     #68
			"Specialist Gloves | Crimson Web `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/specialist_gloves_specialist_webs_red_light_large.f98d18b4fe7ad7e5dec69a61f2c82631a44e4c52.png",#69
			"Specialist Gloves | Mogul `;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DAQ1h3LAVbv6mxFABs3OXNYgJR_Nm1nYGHnuTgDKzYmH9U-s10ktbM8Ij8nVmLpxIuNDztJtLAIAE4YAqG_QTowe69hp-4uZnLy3ti7nZ2tizdnETlhB0dP7Y-heveFwsBuzUGvQ/360fx360f",    #70
			"Specialist Gloves | Buckshot `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/specialist_gloves_specialist_forest_brown_light_large.9006b6eb926c084698116f2c534c963a2f8fccec.png", #71
			"Sport Gloves | Omega `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/sporty_gloves_sporty_black_webbing_yellow_light_large.5d7b101eb7875c41cff58e0fa0c08a49f7303b50.png",         #72
			"Sport Gloves | Vice `;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DAQ1JmMR1osbaqPQJz7ODYfi9W9eO0mJWOqOf9PbDum25V4dB8teXA54vwxgLtqURrYDzydoeWd1JtZ1_Q-1O8yL3r0Je_ucvJy3dk7HJ25C2OnBapwUYbuKd4XdQ/360fx360f",          #73
			"Sport Gloves | Amphibious `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/sporty_gloves_sporty_poison_frog_blue_white_light_large.cc4489cbac59f82ddb18c9a331a98bfd40627ee2.png",    #74
			"Sport Gloves | Bronze Morph `;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DAQ1JmMR1osbaqPQJz7ODYfi9W9eOmm4mYmPnLNanekVRD7cFOjfvE8ILKhVGwogYxDDWiZtHAbFc_YljX_ATox-m9gpHovJjJwXti6XQr4SmJzUaxghlPb7Rt1vTKSVyAR_seu4JUU3Q/360fx360f",  #75
			"Hand Wraps | Cobalt Skulls `;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DfVlxgLQFFibKkJQN3wfLYYgJK7dKyg5KKh8j4NrrFnm5D8fp3i-vT_I_KilihriwvOCyveMX6L1NqOB2NlQ3vg7m6m5To6JnOynRkvCUis3zVn0PmgxFPO-ds0_ydQVzPBPcaTfSBAyeC4p9tCHL9GotlaTc/360fx360f",   #76
			"Hand Wraps | Overprint `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/leather_handwraps_handwrap_leathery_fabric_geometric_blue_light_large.a353dde9306d9be1eafd84331b0bf120142b692f.png",       #77
			"Hand Wraps | Duct Tape `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/leather_handwraps_handwrap_leathery_ducttape_light_large.b18975cd28aee7645dbfd86009884358664e1aa5.png",       #78
			"Hand Wraps | Arboreal `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/leather_handwraps_handwrap_leathery_fabric_green_camo_light_large.2b510ab7fcfd5837f239f378b03216cc3bcf6e3c.png",        #79
			"Moto Gloves | POW! `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/motorcycle_gloves_motorcycle_choco_boom_light_large.37abd7be1296fa17815f7b41a7d063e45b343cab.png",           #80
			"Moto Gloves | Turtle `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/motorcycle_gloves_motorcycle_basic_green_orange_light_large.3e58353974e92bb56f218bb93b4fa77b0639e498.png",         #81
			"Moto Gloves | Transport `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/motorcycle_gloves_motorcycle_yellow_camo_light_large.7ed261be20f42153198256faa761bb0b820b2ef9.png",      #82
			"Moto Gloves | Polygon `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/motorcycle_gloves_motorcycle_trigrid_blue_light_large.5e8f353a222f45406ab0b60e0d68d669953f0e20.png",        #83
			"Driver Gloves | King Snake `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/slick_gloves_slick_snakeskin_white_light_large.f6a54c7a3cf91ecbe0a712bb2126bfe77f86825e.png",   #84
			"Driver Gloves | Imperial Plaid `;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DAX1R3LjtQurWzLhRfwP_BcjZ9_NC3nYS0h-LmI7fUqWZU7Mxkh9bN9J7yjRrhqURoajimcoGWIw5qZF-G8gfqx73qh5Dt7Z-bzSNguyN04yvayhC3n1gSOQLRpPXA/360fx360f",#85
			"Driver Gloves | Overtake `;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DAX1R3LjtQurWzLhRfwP_BcjZ9_8i_gIODkvPLMbfQlWBu59dwhO7EyoHwjF2hpiwwMiukcZjHcFc-YlqB_we5wei-g567usvKz3Rm6XUq5n-OnhKz1BpKabBugaDMVxzAUC3Cr238/360fx360f",     #86
			"Driver Gloves | Racing Green `;https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/slick_gloves_slick_stitched_green_grey_light_large.808fca3933fe16b20eb0cc26bd78fbbc47988dad.png"  #87
			]

			major_medals = [
			"DreamHack Winter 2013 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/4/47/Dreamhack_2013_quarterfinalist_large.png/revision/latest?cb=20140911151520",
			"DreamHack Winter 2013 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/2/28/Dreamhack_2013_semifinalist_large.png/revision/latest?cb=20140911151527",
			"DreamHack Winter 2013 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/c/c4/Dreamhack_2013_finalist_large.png/revision/latest/scale-to-width-down/480?cb=20140911151513",
			"DreamHack Winter 2013 Champion;https://vignette.wikia.nocookie.net/cswikia/images/b/b4/Dreamhack_2013_champion_large.png/revision/latest/scale-to-width-down/480?cb=20140911151456",
			"ESL One: Cologne 2014 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/8/8b/Cologne_trophy_quarterfinalist_large.png/revision/latest/scale-to-width-down/480?cb=20140911151435",
			"ESL One: Cologe 2014 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/e/e8/Cologne_trophy_semifinalist_large.png/revision/latest?cb=20140911151450",
			"ESL One: Cologne 2014 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/2/26/Cologne_trophy_finalist_large.png/revision/latest?cb=20140911151429",
			"ESL One: Cologne 2014 Champion;https://vignette.wikia.nocookie.net/cswikia/images/b/ba/Cologne_trophy_champion_large.png/revision/latest?cb=20140911151422",
			"ESL One: Katowice 2014 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/e/e8/Katowice_2014_quarterfinalist_large.png/revision/latest?cb=20140911151546",
			"ESL One: Katowice 2014 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/75/Katowice_2014_semifinalist_large.png/revision/latest?cb=20140911151552",
			"ESL One: Katowice 2014 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/7/7b/Katowice_2014_finalist_large.png/revision/latest?cb=20140911151540",
			"ESL One: Katowice 2014 Champion;https://vignette.wikia.nocookie.net/cswikia/images/7/79/Katowice_2014_champion_large.png/revision/latest?cb=20140911151533",
			"DreamHack Winter 2014 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/c/cc/Csgo-dhw_2014_quarterfinalist.png/revision/latest?cb=20141121141416",
			"DreamHack Winter 2014 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/b/b1/Csgo-dhw_2014_semifinalist.png/revision/latest?cb=20141121141420",
			"DreamHack Winter 2014 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/1/15/Csgo-dhw_2014_finalist.png/revision/latest?cb=20141121141404",
			"DreamHack Winter 2014 Champion;https://vignette.wikia.nocookie.net/cswikia/images/f/f3/Csgo-dhw_2014_champion.png/revision/latest?cb=20141121141346",
			"ESL One: Katowice 2015 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/4/4e/Csgo-kat_2015_quarterfinalist_large.png/revision/latest?cb=20150306203844",
			"ESL One: Katowice 2015 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/c/cd/Csgo-kat_2015_semifinalist_large.png/revision/latest?cb=20150306203957",
			"ESL One: Katowice 2015 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/6/6a/Csgo-kat_2015_finalist_large.png/revision/latest?cb=20150306203825",
			"ESL One: Katowice 2015 Champion;https://vignette.wikia.nocookie.net/cswikia/images/7/78/Csgo-kat_2015_champion_large.png/revision/latest?cb=20150306203815",
			"ESL One: Cologne 2015 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/5/51/Csgo-col_2015_quarterfinalist_large.png/revision/latest?cb=20150816232457",
			"ESL One: Cologne 2015 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/9/9c/Csgo-col_2015_semifinalist_large.png/revision/latest?cb=20150816232503",
			"ESL One: Cologne 2015 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/c/cc/Csgo-col_2015_finalist_large.png/revision/latest?cb=20150816232451",
			"ESL One: Cologne 2015 Champion;https://vignette.wikia.nocookie.net/cswikia/images/5/5d/Csgo-col_2015_champion_large.png/revision/latest?cb=20150816232444",
			"DreamHack Open Cluj-Napoca 2015 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"DreamHack Open Cluj-Napoca 2015 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"DreamHack Open Cluj-Napoca 2015 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"DreamHack Open Cluj-Napoca 2015 Champion;https://vignette.wikia.nocookie.net/cswikia/images/a/aa/Csgo_trophy_majors.png/revision/latest?cb=20170802120124",
			"MLG Columbus 2016 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"MLG Columbus 2016 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"MLG Columbus 2016 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"MLG Columbus 2016 Champion;https://vignette.wikia.nocookie.net/cswikia/images/a/aa/Csgo_trophy_majors.png/revision/latest?cb=20170802120124",
			"ESL One: Cologne 2016 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"ESL One: Cologne 2016 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"ESL One: Cologne 2016 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"ESL One: Cologne 2016 Champion;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"ELEAGUE Major Atlanta 2017 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"ELEAGUE Major Atlanta 2017 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"ELEAGUE Major Atlanta 2017 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"ELEAGUE Major Atlanta 2017 Champion;https://vignette.wikia.nocookie.net/cswikia/images/a/aa/Csgo_trophy_majors.png/revision/latest?cb=20170802120124",
			"PGL Major Kraków 2017 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"PGL Major Kraków 2017 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"PGL Major Kraków 2017 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"PGL Major Kraków 2017 Champion;https://vignette.wikia.nocookie.net/cswikia/images/a/aa/Csgo_trophy_majors.png/revision/latest?cb=20170802120124",
			"ELEAGUE Major Boston 2018 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"ELEAGUE Major Boston 2018 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"ELEAGUE Major Boston 2018 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"ELEAGUE Major Boston 2018 Champion;https://vignette.wikia.nocookie.net/cswikia/images/a/aa/Csgo_trophy_majors.png/revision/latest?cb=20170802120124",
			"FACEIT Major London 2018 Quarterfinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"FACEIT Major London 2018 Semifinalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"FACEIT Major London 2018 Finalist;https://vignette.wikia.nocookie.net/cswikia/images/7/72/Csgo_trophy_majors_finalists.png/revision/latest?cb=20170802120125",
			"FACEIT Major London 2018 Champion;https://vignette.wikia.nocookie.net/cswikia/images/a/aa/Csgo_trophy_majors.png/revision/latest?cb=20170802120124"
			]

			csgo_pins = [
			"Valeria Phoenix ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFBFh3_baeDx94N2kk4XFw_GhZu-JxzMIvJx007vErduh0Azlr0RoZDv2I4WXJlJvZQrQqVG5xPCv28GYd26wPg/360fx360f",
			"Chroma ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFARowfzFcAJO7c6xkc6PlKSmY-qBxT1QsMEo3eyUrN-j2Qaw-EtuYj_zcdTEI1BoY12D_wO6366x0s8DaT-o/360fx360f",
			"Guardian Elite ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAB10uHMeDxM6dC_gIW0m_bmNL6fwTsI6sEk37zCrY3z3wGx80Q5Nm_1JdfEI1VtZA2B_ge2xr-8jcC_uoOJlyV4eYTAkg/360fx360f",
			"Dust 2 ;https://vignette.wikia.nocookie.net/cswikia/images/8/87/Csgo-collectible-pin-dust2.png/revision/latest?cb=20150228183341",
			"Cache ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFARh0PvNTjFD_tuz2oTewfb1a-qHkG5Qvp0j2OvF9tqmiwCxqkNsNWzwdYaVewU3NA6B-FKggbC4ZK1INMY/360fx360f",
			"Bloodhound ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAVs3PzMeTJX4tiJmIGZkPK6YOiBl25TsJxy0rnDodWsjlbs_hBsam3wJY-Wd1M7YQnU-AO3lLrugIj84sphGd3qgg/360fx360f",
			"Mirage ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAppwfLPdAJO7c6xkc7exfOhZeOEwjkFsJIn07-Zrdzwjgft_hY6Y2n6LIOWIVJqaVCD-AS2366x0kUGiqtn/360fx360f",
			"Inferno ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFA5u1fbafzJ94N2kk4XFx6-mMujTkDgC7ZJ33OyZpN703AO2-kJkYWilIIGSJwI3YA7UqwW8lfCv28HCUj8qrw/360fx360f",
			"Cobblestone ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFARv0fHEdC5W49Kzq4yKhfDxfenQzm0Cv8B03u2SpdyljlHn_UdqMGv0Io6XJ1A7ZA6B_wS6w7u50Zei_MOerINQnmY/360fx360f",
			"Overpass ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAh21uHYcC5R09C3hoeO2aOtZr-DkG1U7Zx037mX89X0jACw_0poNzz0JYfBIFI9aF_R_1O7l7jxxcjrRs2KDss/360fx360f",
			"Office ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAhm1frLdAJO7c6xkc7SlvWnYeuBlGpSsZ0niO-U94_33QDsr0duaz2gItCSdQA2ZV_UrwPq366x0uy4hVrv/360fx360f",
			"Victory ;https://vignette.wikia.nocookie.net/cswikia/images/4/4a/Csgo-collectible-pin-victory.png/revision/latest?cb=20150227180445",
			"Italy ;https://vignette.wikia.nocookie.net/cswikia/images/8/85/Csgo-collectible-pin-italy.png/revision/latest?cb=20150228183354",
			"Militia ;https://vignette.wikia.nocookie.net/counterstrike/images/f/fc/Csgo-collectible-pin-militia-1-.png/revision/latest?cb=20150723154238&path-prefix=ru",
			"Phoenix ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFBdo3PbGeCV94N2kk4XFwPWmNuOFw24DupwoiOyZ8din0AO1_xFsY2HxdobHdwNqY1jWr1m-l_Cv28Ef6RSzKg/360fx360f",
			"Guardian 2 ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAB10uHMeDxM046JmIGZkPK6auyExzwHv5wjjLiSpdis3VewqBdrNW3wcYaUIFU2M1yB_VTtyOi9g4j84spduoEVnw/360fx360f",
			"Guardian ;https://vignette.wikia.nocookie.net/cswikia/images/7/73/Csgo-collectible-pin-guardian.png/revision/latest?cb=20150227180432",
			"Bravo ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAVy0uXHTjFD_tuz2tLSlq-hMe2FwjgAsMN32--So4ql3wXh8hdkMGDwJ9fGdg9sNQqDrgWggbC4lQq_Z1s/360fx360f",
			"Baggage ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAVh1PTJdjh94N2kk4XFlvGlZ-PSxmpQupFwjLGWp97zjgO2rUtrY2ryctCSdgc2ZFzRrAW_wfCv28FfvmDFqw/360fx360f",
			"Tactics ;https://vignette.wikia.nocookie.net/cswikia/images/3/30/Csgo-collectible-pin-tactics.png/revision/latest?cb=20150227180941",
			"Nuke ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAl12Pb3fTxQ69n4ldXZxPagNb6AwWkAusYl2O-W9NWsjQXmrRBqNzv3LY_DJA85NV2CqE_-n7muz2Bucw/360fx360f",
			"Train ;https://vignette.wikia.nocookie.net/cswikia/images/1/1f/Csgo-collectible-pin-train.png/revision/latest?cb=20150228183433",
			"Howl ;https://vignette.wikia.nocookie.net/cswikia/images/b/be/Collectible_pin_howl_large.png/revision/latest?cb=20171220115537",
			"Brigadier General ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAVy2vTJdTRH_uOxkY6Ohfb4DLfQhGxUpsRy2b_HoY2l2wfh-UdqNmv2d9TGIwI5ZgqG8gS_wu-915TuuszOznN9-n51sPQOETc/360fx360f",
			"Aces High ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAZj1uD3eTRF5OO6lZKMkrmhZOOGlG8J7JYg3rCS89rx2VW2qRU-NW7ydoaWdA43Y1jS_FC8yei6m9bi6-xMokL4/360fx360f",
			"Hydra ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFA951-HJTjFD_tuz2tPSxK7xZeLVxT1SupYk07DHp9uk2lHj-xc-ZjugJNfHdA5rZwvR_FaggbC4FLZg8pw/256fx256f",
			"Easy Peasy ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAJhwOr3YThD_8WJmIGZkPK6Zb-ClzkHvZUn07yZ84mn3gbt-Us6YDumIYKXcVI8ZVmErla2lLq-14j84srPLgJ0eg/360fx360f",
			"Wildfire ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFBBp3_fOeC9H09C3hoeO2fWgZerVlGlXvpJwiLCZ9Nv23lHl-RVpZGvxJ9PBJgVtYFDZ-ALtxunxxcjrZBZc5XA/360fx360f",
			"Inferno 2 ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFA5u1fbafzJ9vuO6lZKMkrmtN-6GwGgJ65cn37qZ8dnx2lbl-xdpMDyhctPEJFQ2aArQ8we7xb29m9bi6xzTLb2A/360fx360f",
			"Welcome to the Clutch ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFBBl3_DHfDh9-NOJgIiOqPT4Jq_SnlRd6dd2j6eXo9703Vay_hJtZj33I4HHJwU9M17U-QO2ybvv0Je-uZmbyHRiuiF2-z-DyCV-0Dwc/360fx360f",
			"Death Sentence ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFANl0ufATi5H4sizmoOOqPv1IbzU2DlVu5JwjuyTpdr2iQK1rRFuMjiico-cJ1A4YV_Y-1fsxb_u1J7q7Z_XiSw01vuTbO4/360fx360f",
			"Guardian 3 ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFAB10uHMeDxM04-JmIGZkPK6N--Fz2pUvsZy07HEpY-i3VLhrUppNmD0doeRdlM5NV_Q-1C_krq60Yj84soQnOvujw/360fx360f",
			"Canals ;https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9Q1LO5kNoBhSQl-fROuh28rQR1R2KQFoprOrFARh3fLEYgJO7c6xkc6NzvSlaurSwTwBv5EmibvCod-gjgzh-UU-Mm6idYOScQE7Y1yCqwfr366x0oLwztIh/360fx360f"
			]

			case_items_knives_and_gloves = [
			case_items[0],
			case_items[1],
			case_items[15],
			case_items[16],
			case_items[17],
			case_items[31],
			case_items[32],
			case_items[33],
			case_items[34],
			case_items[35],
			case_items[64],
			case_items[65],
			case_items[66],
			case_items[67],
			case_items[68],
			case_items[69],
			case_items[70],
			case_items[71],
			case_items[72],
			case_items[73],
			case_items[74],
			case_items[75],
			case_items[76],
			case_items[77],
			case_items[78],
			case_items[79],
			case_items[80],
			case_items[81],
			case_items[82],
			case_items[83],
			case_items[84],
			case_items[85],
			case_items[86],
			case_items[87]
			]

			case_items_covert = [
			case_items[2],
			case_items[4],
			case_items[5],
			case_items[36],
			case_items[37],
			case_items[46],
			case_items[47]
			]

			case_items_classified = [
			case_items[3],
			case_items[13],
			case_items[14],
			case_items[38],
			case_items[39],
			case_items[40],
			case_items[48],
			case_items[49],
			case_items[50]
			]

			case_items_restricted = [
			case_items[11],
			case_items[12],
			case_items[18],
			case_items[19],
			case_items[20],
			case_items[21],
			case_items[38],
			case_items[51],
			case_items[52],
			case_items[53],
			case_items[54],
			case_items[55]
			]

			case_items_milspec = [
			case_items[6],
			case_items[7],
			case_items[8],
			case_items[9],
			case_items[10],
			case_items[22],
			case_items[23],
			case_items[24],
			case_items[25],
			case_items[26],
			case_items[27],
			case_items[28],
			case_items[29],
			case_items[30],
			case_items[41],
			case_items[42],
			case_items[43],
			case_items[44],
			case_items[45],
			case_items[56],
			case_items[57],
			case_items[58],
			case_items[59],
			case_items[60],
			case_items[61],
			case_items[62],
			case_items[63]
			]

			case_items_condition = [
			"Factory New",
			"Minimal Wear",
			"Field-Tested",
			"Well-Worn",
			"Battle-Scarred"
			]

			#Case Opening Script

			# - StatTrak - #

			case_drop_statrak = random.randint(0,10)
			if case_drop_statrak == 10: stattrak = "StatTrak "
			else: stattrak = ""

			# - Drop Quality and Condition - #

			random_drop = random.randint(0,100)

			if random_drop <= 1: #Knives & Gloves - 1% Chance

				stattrak = ""
				case_drop = random.choice(case_items_knives_and_gloves)
				case_drop_condition = case_items_condition[0]

			elif random_drop <= 6: #Covert - 5% Chance

				case_drop = random.choice(case_items_covert)
				case_drop_condition =  random.choice(case_items_condition)

			elif random_drop <= 17: #Classified - 11% Chance

				case_drop = random.choice(case_items_classified)
				case_drop_condition =  random.choice(case_items_condition)

			elif random_drop <= 37: #Restricted - 20% Chance

				case_drop = random.choice(case_items_restricted)
				case_drop_condition =  random.choice(case_items_condition)

			else: #Mil-Spec - 63% Chance

				case_drop = random.choice(case_items_milspec)
				case_drop_condition =  random.choice(case_items_condition)

			case_drop_s = case_drop.split(";")
			opened_item = stattrak + "({}) ".format(case_drop_condition) + case_drop_s[0]

			#Case Opening Message

			case_opening_message_1 = ":hourglass_flowing_sand:│ Opening Case..."
			case_opening_message_2 = ":hourglass:│ Opening Case.. "

			if ctx.author.id != 203299786382639104: # If not Rigged User

				#Normal User Drop Message

				if rigged_argument == "normal_drop_rate":

					case_drop_message = "**<:csgocase:433064927645925386> You have received:**\n `{}".format(opened_item)

				elif rigged_argument.lower() == "trophy":

					case_drop = random.choice(major_medals)
					case_drop_s = case_drop.split(";")
					case_drop_message = "**<:csgocase:433064927645925386> You have received:**\n `{}".format(case_drop_s[0]) + " Trophy`"

				elif rigged_argument.lower() == "pin":

					case_drop = random.choice(csgo_pins)
					case_drop_s = case_drop.split(";")
					case_drop_message = "**<:csgocase:433064927645925386> You have received:**\n `{}".format(case_drop_s[0]) + "Pin`"

				else:

					await ctx.send(":warning: No such case!")
					return

			else:
				#Case Opening Rigged User Settings and Message:
				if rigged_argument == "0":
					
					stattrak = ""
					case_drop = random.choice(case_items_knives_and_gloves)
					case_drop_s = case_drop.split(";")
					opened_item = stattrak + "({}) {}".format(case_items_condition[0], case_drop_s[0])
					case_drop_message = "**<:csgocase:433064927645925386> You have received:**\n `{}".format(opened_item)

				elif rigged_argument == "1":

					case_drop = random.choice(case_items_milspec)
					case_drop_s = case_drop.split(";")
					opened_item = stattrak + "({}) {}".format(case_drop_condition, case_drop_s[0])
					case_drop_message = "**<:csgocase:433064927645925386> You have received:**\n `{}".format(opened_item)

				elif rigged_argument == "2":

					case_drop = random.choice(case_items_restricted)
					case_drop_s = case_drop.split(";")
					opened_item = stattrak + "({}) {}".format(case_drop_condition, case_drop_s[0])
					case_drop_message = "**<:csgocase:433064927645925386> You have received:**\n `{}".format(opened_item)

				elif rigged_argument == "3":

					case_drop = random.choice(case_items_classified)
					case_drop_s = case_drop.split(";")
					opened_item = stattrak + "({}) {}".format(case_drop_condition, case_drop_s[0])
					case_drop_message = "**<:csgocase:433064927645925386> You have received:**\n `{}".format(opened_item)

				elif rigged_argument == "4":

					case_drop = random.choice(case_items_covert)
					case_drop_s = case_drop.split(";")
					opened_item = stattrak + "({}) {}".format(case_drop_condition, case_drop_s[0])
					case_drop_message = "**<:csgocase:433064927645925386> You have received:**\n `{}".format(opened_item)

				elif rigged_argument.lower() == "trophy": #normal

					case_drop = random.choice(major_medals)
					case_drop_s = case_drop.split(";")
					case_drop_message = "**<:csgocase:433064927645925386> You have received:**\n `{}".format(case_drop_s[0]) + " Trophy`"

				elif rigged_argument.lower() == "pin": #Normal

					case_drop = random.choice(csgo_pins)
					case_drop_s = case_drop.split(";")
					case_drop_message = "**<:csgocase:433064927645925386> You have received:**\n `{}".format(case_drop_s[0]) + "Pin`"

				elif rigged_argument == "normal_drop_rate":

					case_drop_message = "**<:csgocase:433064927645925386> You have received:**\n `{}".format(opened_item)

			embed = discord.Embed(title="", description=case_drop_message, colour=member.colour)
			embed.set_author(icon_url=member.avatar_url, name=str(member))
			embed.set_image(url=case_drop_s[1])
			msg = await ctx.send(case_opening_message_1)
			await asyncio.sleep(0.5)
			await msg.edit(content=case_opening_message_2)
			await asyncio.sleep(0.5)
			await msg.edit(content=case_opening_message_1)
			await asyncio.sleep(0.5)
			await msg.edit(content=case_opening_message_2)
			await asyncio.sleep(0.5)
			await msg.edit(content=case_opening_message_1)
			await asyncio.sleep(0.5)									
			await msg.edit(content="", embed=embed)


def setup(bot):
	bot.add_cog(CaseOpeningCog(bot))
