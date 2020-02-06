from enum import Enum

'''
List of all modifiers in EU4 and what modifier look like when actually displayed to the client. 

I might be missing some as I used the list given in common/custom_ideas
'''
class ModifierList(Enum):

    # Adm ideas
    global_tax_modifier = ('PercentModifier', 'National Tax Modifier')
    production_efficiency = ('PercentModifier', 'Production Efficiency')
    global_unrest = ('FloatModifier', 'National Unrest')
    stability_cost_modifier = ('PercentModifier', 'Stability Cost Modifier')
    missionaries = ('IntegerModifier', 'Missionaries')
    inflation_reduction = ('FloatModifier', 'Yearly Inflation Reduction')
    inflation_action_cost = ('PercentModifier', 'Reduce Inflation Cost')
    interest = ('FloatModifier', 'Interest per Annum')
    build_cost = ('PercentModifier', 'Construction Cost')
    development_cost = ('PercentModifier', 'Development Cost')
    global_missionary_strength = ('PercentModifier', 'Missionary Strength')
    prestige = ('FloatModifier', 'Yearly Prestige')
    prestige_decay = ('PercentModifier', 'Prestige Decay')
    legitimacy = ('FloatModifier', 'Yearly Legitimacy')
    horde_unity = ('FloatModifier', 'Yearly Horde Unity')
    devotion = ('FloatModifier', 'Yearly Devotion')
    republican_tradition = ('FloatModifier', 'Yearly Republican Tradition')
    technology_cost = ('PercentModifier', 'Technology Cost')
    idea_cost = ('PercentModifier', 'Idea Cost')
    advisor_cost = ('PercentModifier', 'Advisor Costs')
    advisor_pool = ('IntegerModifier', 'Possible Advisors')
    tolerance_own = ('FloatModifier', 'Tolerance of the True Faith')
    tolerance_heretic = ('FloatModifier', 'Tolerance of Heretics')
    tolerance_heathen = ('FloatModifier', 'Tolerance of Heathens')
    heir_chance = ('PercentModifier', 'Chance of new heir')
    enemy_core_creation = ('PercentModifier', 'Hostile Core Creation Cost on us')
    core_creation = ('PercentModifier', 'Core Creation Cost')
    vassal_income = ('PercentModifier', 'Income from Vassals')
    religious_unity = ('PercentModifier', 'Religious Unity')
    global_autonomy = ('PercentModifier', 'Monthly Autonomy Change')
    imperial_authority = ('PercentModifier', 'Imperial Authority')
    free_adm_policy = ('IntegerModifier', 'Administrative free policies')
    possible_adm_policy = ('IntegerModifier', 'Administrative possible policies')
    yearly_harmony = ('FloatModifier', 'Yearly Harmony')
    harmonization_speed = ('PercentModifier', 'Religious Harmonization Speed')
    meritocracy = ('FloatModifier', 'Yearly Meritocracy')
    monarch_admin_power = ('IntegerModifier', 'Monarch Administrative Skill')
    max_absolutism = ('FloatModifier', 'Maximum Absolutism')
    yearly_absolutism = ('FloatModifier', 'Yearly Absolutism')
    administrative_efficiency = ('PercentModifier', 'Administrative Efficiency')
    institution_spread_from_true_faith = ('PercentModifier', 'Institution Spread in True Faith Provinces')
    global_institution_spread = ('PercentModifier', 'Institution Spread')
    embracement_cost = ('PercentModifier', 'Institution Embracement Cost')
    max_states = ('FloatModifier', 'Number of States')
    church_power_modifier = ('PercentModifier', 'Church Power')
    yearly_corruption = ('FloatModifier', 'Yearly Corruption')
    caravan_power = ('PercentModifier', 'Caravan Power')
    monthly_fervor_increase = ('FloatModifier', 'Monthly Fervor')
    global_trade_goods_size_modifier = ('PercentModifier', 'Goods Produced')
    adm_tech_cost_modifier = ('PercentModifier', 'Administrative Technology Cost')
    build_time = ('PercentModifier', 'Construction Time')
    state_maintenance_modifier = ('PercentModifier', 'State Maintenance')
    autonomy_change_time = ('PercentModifier', 'Autonomy Change Cooldown')
    years_of_nationalism = ('FloatModifier', 'Years of Separatism')
    female_advisor_chance = ('PercentModifier', 'Female Advisor Chance')
    global_heretic_missionary_strength = ('PercentModifier', 'Missionary Strength vs Heretics')
    monthly_piety = ('PercentModifier', 'Monthly Piety')
    same_culture_advisor_cost = ('PercentModifier', 'Cost of Advisors with Ruler\'s Culture')
    possible_policy = ('IntegerModifier', 'Possible Policies')
    reform_progress_growth = ('PercentModifier', 'Reform Progress Growth')
    no_religion_penalty = ('BooleanModifier', 'No penalty from Negative Religious Tolerance')
    yearly_tribal_allegiance = ('FloatModifier', 'Yearly Tribal Allegiance')
    imperial_mandate = ('FloatModifier', 'Mandate Growth Modifier')
    innovativeness_gain = ('PercentModifier', 'Innovativeness Gain')
    missionary_maintenance_cost = ('PercentModifier', 'Missionary Maintenance Cost')
    cb_on_religious_enemies = ('BooleanModifier', 'Permanent Casus Belli against Neighboring Heathens and Heretics')
    cb_on_overseas = ('BooleanModifier', 'Can Fabricate Claim Overseas in Trade Company Regions')
    center_of_trade_upgrade_cost = ('PercentModifier', 'Center of Trade Upgrade Cost')
    colonist_placement_chance = ('PercentModifier', 'Settler Chance')

    # Dip ideas
    may_establish_frontier = ('BooleanModifier', 'May Establish Siberian Frontiers')
    global_sailors_modifier = ('PercentModifier', 'National Sailors Modifier')
    sailors_recovery_speed = ('PercentModifier', 'Sailor Recovery Speed')
    may_perform_slave_raid = ('BooleanModifier', 'May Raid Coasts')
    warscore_cost_vs_other_religion = ('PercentModifier', 'Warscore Cost vs Other Religions')
    war_taxes_cost_modifier = ('PercentModifier', 'War Taxes Cost')
    monarch_diplomatic_power = ('FloatModifier', 'Monarch Diplomatic Skill')
    liberty_desire_from_subject_development = ('PercentModifier', 'Liberty desire from subject development')
    reduced_liberty_desire_on_same_continent = ('PercentModifier', 'Liberty desire in same continent subjects')
    naval_tradition_from_battle = ('PercentModifier', 'Naval Tradition From Battles')
    capture_ship_chance = ('PercentModifier', 'Chance to Capture Enemy Ships')
    sunk_ship_morale_hit_recieved = ('PercentModifier', 'Morale Hit When Losing a Ship')
    global_naval_engagement_modifier = ('PercentModifier', 'Global Naval Engagement')
    global_ship_trade_power = ('PercentModifier', 'Ship Trade Power')
    native_assimilation = ('PercentModifier', 'Native Assimilation')
    native_uprising_chance = ('PercentModifier', 'Native Uprising Chance')
    reduced_liberty_desire = ('PercentModifier', 'Liberty Desire in Subjects')
    migration_cooldown = ('PercentModifier', 'Migration Cooldown')
    envoy_travel_time = ('PercentModifier', 'Envoy Travel Time')
    province_warscore_cost = ('PercentModifier', 'Province Warscore Cost')
    dip_tech_cost_modifier = ('PercentModifier', 'Diplomatic Technology Cost')
    papal_influence = ('FloatModifier', 'Yearly Papal Influence')
    trade_range_modifier = ('PercentModifier', 'Trade Range')
    auto_explore_adjacent_to_colony = ('BooleanModifier', 'Automatically Discover Adjacent When a Colony is Built')
    unjustified_demands = ('PercentModifier', 'Unjustified Demands')
    rebel_support_efficiency = ('PercentModifier', 'Rebel Support Efficiency')
    placed_merchant_power = ('FloatModifier', 'Merchant Trade Power')
    global_own_trade_power = ('PercentModifier', 'Domestic Trade Power')
    recover_navy_morale_speed = ('PercentModifier', 'Recover Navy Morale Speed')
    global_foreign_trade_power = ('PercentModifier', 'Trade Power Abroad')
    improve_relation_modifier = ('PercentModifier', 'Improve Relations')
    possible_condottieri = ('PercentModifier', 'Possible Condottieri')
    naval_attrition = ('PercentModifier', 'Naval Attrition')
    num_accepted_cultures = ('IntegerModifier', 'Max Promoted Cultures')
    culture_conversion_cost = ('PercentModifier', 'Culture Conversion Cost')
    naval_morale = ('PercentModifier', 'Morale of Navies')
    trade_efficiency = ('PercentModifier', 'Trade Efficiency')
    global_trade_power = ('PercentModifier', 'Global Trade Power')
    global_prov_trade_power_modifier = ('PercentModifier', 'Provincial Trade Power Modifier')
    trade_steering = ('PercentModifier', 'Trade Steering')
    global_tariffs = ('PercentModifier', 'Global Tariffs')
    diplomatic_reputation = ('IntegerModifier', 'Diplomatic Reputation')
    diplomatic_upkeep = ('IntegerModifier', 'Diplomatic Relations')
    merchants = ('IntegerModifier', 'Merchant')
    colonists = ('IntegerModifier', 'Colonist')
    diplomats = ('IntegerModifier', 'Diplomat')
    naval_maintenance_modifier = ('PercentModifier', 'Naval Maintenance Modifier')
    naval_forcelimit_modifier = ('PercentModifier', 'Naval Force Limit Modifier')
    ship_durability = ('PercentModifier', 'Ship Durability')
    war_exhaustion = ('FloatModifier', 'Monthly War Exhaustion')
    war_exhaustion_cost = ('PercentModifier', 'Cost of Reducing War Exhaustion')
    navy_tradition = ('FloatModifier', 'Yearly Navy Tradition')
    navy_tradition_decay = ('PercentModifier', 'Yearly Navy Tradition Decay')
    leader_naval_fire = ('IntegerModifier', 'Naval Leader Fire')
    leader_naval_shock = ('IntegerModifier', 'Naval Leader Shock')
    leader_naval_manuever = ('IntegerModifier', 'Naval Leader Maneuver')
    spy_offence = ('PercentModifier', 'Spy Network Construction')
    global_spy_defence = ('PercentModifier', 'Foreign Spy Detection')
    global_ship_recruit_speed = ('PercentModifier', 'Shipbuilding Time')
    blockade_efficiency = ('PercentModifier', 'Blockade Efficiency')
    embargo_efficiency = ('PercentModifier', 'Embargo Efficiency')
    prestige_from_naval = ('PercentModifier', 'Prestige from Naval Battles')
    range = ('PercentModifier', 'Colonial Range')
    global_colonial_growth = ('IntegerModifier', 'Global Settler Increase')
    ae_impact = ('PercentModifier', 'Aggressive Expansion Impact')
    privateer_efficiency = ('PercentModifier', 'Privateer Efficiency')
    diplomatic_annexation_cost = ('PercentModifier', 'Diplomatic Annexation Cost')
    heavy_ship_cost = ('PercentModifier', 'Heavy Ship Cost')
    light_ship_cost = ('PercentModifier', 'Light Ship Cost')
    galley_cost = ('PercentModifier', 'Galley Cost')
    transport_cost = ('PercentModifier', 'Transport Cost')
    heavy_ship_power = ('PercentModifier', 'Heavy Ship Combat Ability')
    light_ship_power = ('PercentModifier', 'Light Ship Combat Ability')
    galley_power = ('PercentModifier', 'Galley Combat Ability')
    free_dip_policy = ('IntegerModifier', 'Diplomatic free policies')
    possible_dip_policy = ('IntegerModifier', 'Diplomatic possible policies')
    sailor_maintenance_modifer = ('PercentModifier', 'Sailor Maintenance')
    justify_trade_conflict_cost = ('PercentModifier', 'Cost to Justify Trade Conflict')
    fabricate_claims_cost = ('PercentModifier', 'Cost to Fabricate Claims')
    idea_claim_colonies = ('BooleanModifier', 'Can fabricate claims on any overseas province, ' +
                                              'provided it is overseas for its owner')
    global_ship_cost = ('PercentModifier', 'Ship Cost')
    may_explore = ('BooleanModifier', 'May Recruit Explorers and Conquistadors')
    cb_on_primitives = ('BooleanModifier', 'Can Fabricate Claim Overseas in Colonial Region')
    power_projection_from_insults = ('PercentModifier', 'Power Projection from Insults')
    own_coast_naval_combat_bonus = ('IntegerModifier', 'Naval Combat Bonus off Owned Coast')
    pr_captains_influence = ('FloatModifier', 'Monthly Captains influence')
    can_fabricate_for_vassals = ('BooleanModifier', 'May Fabricate Claims for Subjects')
    reduced_stab_impacts = ('BooleanModifier', 'Lowered Impact on Stability from Diplomatic Actions')
    expel_minorities_cost = ('PercentModifier', 'Expel Minorities Cost')
    sea_repair = ('BooleanModifier', 'Ships Can Repair in Coastal Sea Zones')
    naval_tradition_from_trade = ('PercentModifier', 'Naval Tradition from Protecting Trade')
    global_ship_repair = ('PercentModifier', 'Global Ship Repair')
    admiral_cost = ('PercentModifier', 'Admiral Cost')

    # Mil ideas
    may_recruit_female_generals = ('BooleanModifier', 'May Recruit Female Generals')
    mercenary_discipline = ('PercentModifier', 'Mercenary Discipline')
    rival_border_fort_maintenance = ('PercentModifier', 'Fort Maintenance on Border with Rival')
    siege_blockade_progress = ('IntegerModifier', 'Blockade Impact on Siege')
    cav_to_inf_ratio = ('PercentModifier', 'Cavalry to Infantry Ratio')
    artillery_bonus_vs_fort = ('FloatModifier', 'Artillery Bonus vs Fort')
    monarch_military_power = ('FloatModifier', 'Monarch Military Skill')
    backrow_artillery_damage = ('PercentModifier', 'Artillery Damage from Back Row')
    harsh_treatment_cost = ('PercentModifier', 'Harsh Treatment Cost')
    fire_damage_received = ('PercentModifier', 'Fire Damage Received')
    shock_damage_received = ('PercentModifier', 'Shock Damage Received')
    cavalry_flanking = ('PercentModifier', 'Cavalry Flanking Ability')
    shock_damage = ('PercentModifier', 'Land Shock Damage')
    fire_damage = ('PercentModifier', 'Land Fire Damage')
    movement_speed = ('PercentModifier', 'Movement Speed')
    army_tradition_from_battle = ('PercentModifier', 'Army Tradition from Battles')
    monthly_militarized_society = ('FloatModifier', 'Militarization of State')
    reinforce_cost_modifier = ('PercentModifier', 'Reinforce Cost')
    loot_amount = ('PercentModifier', 'Looting Speed')
    garrison_size = ('PercentModifier', 'Garrison Size')
    global_garrison_growth = ('PercentModifier', 'National Garrison Growth')
    # does the same thing as above. IDK why only RIGA uses this one
    garrison_growth = ('PercentModifier', 'National Garrison Growth')
    land_attrition = ('PercentModifier', 'Land Attrition')
    mil_tech_cost_modifier = ('PercentModifier', 'Military Technology Cost')
    free_leader_pool = ('IntegerModifier', 'Leader(s) Without Upkeep')
    global_regiment_cost = ('PercentModifier', 'Regiment Costs')
    mercenary_cost = ('PercentModifier', 'Mercenary Cost')
    recover_army_morale_speed = ('PercentModifier', 'Recover Army Morale Speed')
    artillery_fire = ('FloatModifier', 'Artillery Fire')
    land_morale = ('PercentModifier', 'Morale of Armies')
    discipline = ('PercentModifier', 'Discipline')
    land_maintenance_modifier = ('PercentModifier', 'Land Maintenance Modifier')
    merc_maintenance_modifier = ('PercentModifier', 'Mercenary Maintenance')
    possible_mercenaries = ('PercentModifier', 'Available Mercenaries')
    land_forcelimit_modifier = ('PercentModifier', 'Land Force Limit Modifier')
    global_manpower_modifier = ('PercentModifier', 'National Manpower Modifier')
    manpower_recovery_speed = ('PercentModifier', 'Manpower Recovery Speed')
    reinforce_speed = ('PercentModifier', 'Reinforce Speed')
    hostile_attrition = ('FloatModifier', 'Attrition for Enemies')
    army_tradition = ('FloatModifier', 'Yearly Army Tradition')
    army_tradition_decay = ('PercentModifier', 'Yearly Army Tradition Decay')
    leader_land_fire = ('IntegerModifier', 'Land Leader Fire')
    leader_land_shock = ('IntegerModifier', 'Land Leader Shock')
    leader_land_manuever = ('IntegerModifier', 'Land Leader Maneuver')
    leader_siege = ('IntegerModifier', 'Land Leader Siege')
    global_regiment_recruit_speed = ('PercentModifier', 'Recruitment Time')
    prestige_from_land = ('PercentModifier', 'Prestige from Land battles')
    defensiveness = ('PercentModifier', 'Fort Defense')
    siege_ability = ('PercentModifier', 'Siege Ability')
    vassal_forcelimit_bonus = ('PercentModifier', 'Vassal Force Limit Contribution')
    infantry_power = ('PercentModifier', 'Infantry Combat Ability')
    cavalry_power = ('PercentModifier', 'Cavalry Combat Ability')
    artillery_power = ('PercentModifier', 'Artillery Combat Ability')
    infantry_cost = ('PercentModifier', 'Infantry Cost')
    cavalry_cost = ('PercentModifier', 'Cavalry Cost')
    artillery_cost = ('PercentModifier', 'Artillery Cost')
    fort_maintenance_modifier = ('PercentModifier', 'Fort Maintenance')
    amount_of_banners = ('PercentModifier', 'Possible Manchu banners')
    global_supply_limit_modifier = ('PercentModifier', 'Supply Limit Modifier')
    free_mil_policy = ('IntegerModifier', 'Military free policies')
    possible_mil_policy = ('IntegerModifier', 'Military possible policies')
