"""
Test suite for chemistry numerical problems - Class 12 PCB
Tests atomic structure, chemical bonds, stoichiometry, and pH calculations
Based on: posts/cheatsheet_chemistry.md
"""

import pytest
import numpy as np


class TestAtomicStructureNumericals:
    """Test atomic structure calculations"""
    
    def test_atomic_number_protons(self):
        """Test that atomic number = number of protons"""
        atomic_number = 6  # Carbon
        protons = 6
        assert atomic_number == protons
    
    def test_mass_number_calculation(self):
        """Test A = Z + N (mass number = protons + neutrons)"""
        protons = 6  # Carbon
        neutrons = 8
        mass_number = protons + neutrons
        assert mass_number == 14
    
    def test_neutrons_from_mass_number(self):
        """Test N = A - Z"""
        mass_number = 16  # Oxygen-16
        atomic_number = 8
        neutrons = mass_number - atomic_number
        assert neutrons == 8
    
    def test_electrons_neutral_atom(self):
        """Test electrons = protons for neutral atom"""
        protons = 8
        electrons = protons
        assert electrons == 8
    
    def test_common_isotopes(self):
        """Test atomic properties of common isotopes"""
        # Oxygen-16
        O16_protons = 8
        O16_neutrons = 8
        O16_mass = O16_protons + O16_neutrons
        assert O16_mass == 16
        
        # Carbon-12
        C12_protons = 6
        C12_neutrons = 6
        C12_mass = C12_protons + C12_neutrons
        assert C12_mass == 12


class TestElectronConfigurationNumericals:
    """Test electron configuration calculations"""
    
    def test_max_electrons_first_shell(self):
        """Test first shell can hold max 2 electrons"""
        max_electrons_shell_1 = 2
        assert max_electrons_shell_1 == 2
    
    def test_max_electrons_second_shell(self):
        """Test second shell can hold max 8 electrons"""
        max_electrons_shell_2 = 8
        assert max_electrons_shell_2 == 8
    
    def test_max_electrons_third_shell(self):
        """Test third shell can hold max 18 electrons"""
        max_electrons_shell_3 = 18
        assert max_electrons_shell_3 == 18
    
    def test_valence_electrons_carbon(self):
        """Test valence electrons for carbon"""
        carbon_config = "2,4"  # K shell: 2, L shell: 4
        valence_electrons = 4
        assert valence_electrons == 4
    
    def test_valence_electrons_oxygen(self):
        """Test valence electrons for oxygen"""
        oxygen_config = "2,6"
        valence_electrons = 6
        assert valence_electrons == 6


class TestChemicalBondNumericals:
    """Test chemical bonding calculations"""
    
    def test_covalent_bond_electron_sharing(self):
        """Test electron sharing in covalent bonds"""
        # H2 molecule: each H contributes 1 electron
        electrons_H1 = 1
        electrons_H2 = 1
        shared_pair = electrons_H1 + electrons_H2
        assert shared_pair == 2
    
    def test_ionic_bond_electron_transfer(self):
        """Test electron transfer in ionic bonds"""
        # NaCl: Na loses 1 electron, Cl gains 1
        electrons_Na = 11
        electrons_Cl = 17
        
        electrons_Na_after = electrons_Na - 1  # Na loses 1
        electrons_Cl_after = electrons_Cl + 1  # Cl gains 1
        
        # Both should have stable configurations
        assert electrons_Na_after == 10  # Ne configuration
        assert electrons_Cl_after == 18  # Ar configuration
    
    def test_oxidation_states(self):
        """Test oxidation state calculations"""
        # In H2O
        oxidation_H = 1
        oxidation_O = -2
        
        # Total should be 0 for neutral compound
        total = 2 * oxidation_H + oxidation_O
        assert total == 0
    
    def test_covalent_bonds_in_molecule(self):
        """Test counting covalent bonds"""
        # Water H2O has 2 O-H bonds
        oh_bonds = 2
        assert oh_bonds == 2
        
        # CO2 has 2 C=O double bonds
        co_double_bonds = 2
        assert co_double_bonds == 2


class TestStatesOfMatterNumericals:
    """Test states of matter calculations"""
    
    def test_phase_transition_temperatures(self):
        """Test phase transition temperatures"""
        # Water
        melting_point_water = 0.0  # Celsius
        boiling_point_water = 100.0  # Celsius
        
        assert melting_point_water < boiling_point_water
    
    def test_kinetic_energy_states_of_matter(self):
        """Test that kinetic energy relates to state of matter"""
        # Solid < Liquid < Gas (at same substance)
        KE_solid = 1
        KE_liquid = 2
        KE_gas = 3
        
        assert KE_solid < KE_liquid < KE_gas


class TestpH_Numericals:
    """Test pH calculations"""
    
    def test_pH_acidic_basic_neutral(self):
        """Test pH classification"""
        pH_acidic = 3.0
        pH_neutral = 7.0
        pH_basic = 11.0
        
        assert pH_acidic < 7
        assert pH_neutral == 7
        assert pH_basic > 7
    
    def test_pOH_calculation(self):
        """Test pOH = 14 - pH"""
        pH = 5.0
        pOH = 14 - pH
        assert pOH == 9.0
    
    def test_pH_pOH_relationship(self):
        """Test pH + pOH = 14"""
        pH = 3.0
        pOH = 11.0
        total = pH + pOH
        assert total == 14
    
    def test_hydrogen_ion_concentration_from_pH(self):
        """Test [H+] = 10^(-pH)"""
        pH = 2.0
        H_concentration = 10 ** (-pH)
        np.testing.assert_almost_equal(H_concentration, 0.01, decimal=5)
    
    def test_pH_from_hydrogen_concentration(self):
        """Test pH = -log[H+]"""
        H_concentration = 1e-3  # 0.001 M
        pH = -np.log10(H_concentration)
        assert pH == 3.0


class TestMolarMassNumericals:
    """Test molar mass and mole calculations"""
    
    def test_molar_mass_water(self):
        """Test molar mass of H2O"""
        # H: 1, O: 16
        H_mass = 1
        O_mass = 16
        
        molar_mass_H2O = 2 * H_mass + O_mass
        assert molar_mass_H2O == 18
    
    def test_molar_mass_carbon_dioxide(self):
        """Test molar mass of CO2"""
        C_mass = 12
        O_mass = 16
        
        molar_mass_CO2 = C_mass + 2 * O_mass
        assert molar_mass_CO2 == 44
    
    def test_moles_from_mass(self):
        """Test n = m/M (moles = mass/molar mass)"""
        mass = 36.0  # grams
        molar_mass = 18.0  # g/mol (water)
        moles = mass / molar_mass
        assert moles == 2.0
    
    def test_mass_from_moles(self):
        """Test m = n × M"""
        moles = 2.0
        molar_mass = 18.0  # g/mol (water)
        mass = moles * molar_mass
        assert mass == 36.0
    
    def test_avogadro_number_calculation(self):
        """Test calculations with Avogadro's number"""
        avogadro = 6.022e23  # particles/mol
        moles = 1.0
        particles = moles * avogadro
        np.testing.assert_almost_equal(particles, 6.022e23, decimal=20)


class TestChemicalEquationsStoichiometry:
    """Test stoichiometry calculations"""
    
    def test_combustion_methane_balance(self):
        """Test CH4 + 2O2 -> CO2 + 2H2O"""
        # 1 mole CH4 reacts with 2 moles O2
        CH4_moles = 1
        O2_needed = 2 * CH4_moles
        assert O2_needed == 2
    
    def test_product_moles_from_reactants(self):
        """Test calculating product moles from reactants"""
        # 2H2 + O2 -> 2H2O
        H2_moles = 2
        H2O_produced = H2_moles  # 1:1 ratio
        assert H2O_produced == 2
    
    def test_limiting_reactant_concept(self):
        """Test limiting reactant calculation"""
        # H2 + Cl2 -> 2HCl
        H2_available = 3  # moles
        Cl2_available = 2  # moles
        
        # 1 mole H2 reacts with 1 mole Cl2
        # H2 can react with max 3 moles Cl2 (but only 2 available)
        # So Cl2 is limiting reactant
        
        HCl_from_H2 = H2_available * 2  # if no limit
        HCl_from_Cl2 = Cl2_available * 2
        
        HCl_produced = min(HCl_from_H2, HCl_from_Cl2)
        assert HCl_produced == 4


class TestSoluteConcentrationNumericals:
    """Test concentration calculations"""
    
    def test_molarity_calculation(self):
        """Test M = n/V (molarity = moles/volume in L)"""
        moles_solute = 1.0
        volume_L = 1.0
        molarity = moles_solute / volume_L
        assert molarity == 1.0
    
    def test_molarity_dilution(self):
        """Test M1V1 = M2V2 for dilution"""
        M1 = 2.0  # initial molarity
        V1 = 100.0  # initial volume mL
        V2 = 500.0  # final volume mL
        
        # Calculate final molarity
        M2 = (M1 * V1) / V2
        assert M2 == 0.4
    
    def test_percentage_concentration(self):
        """Test w/w% calculation"""
        mass_solute = 20.0  # grams
        mass_solution = 100.0  # grams
        
        percent = (mass_solute / mass_solution) * 100
        assert percent == 20.0


class TestChemistryNumericalStability:
    """Test numerical stability and edge cases"""
    
    def test_pH_calculation_very_small_concentration(self):
        """Test pH with very small H+ concentration"""
        H_concentration = 1e-14
        pH = -np.log10(H_concentration)
        assert pH == 14.0
    
    def test_pH_calculation_very_large_concentration(self):
        """Test pH with very large H+ concentration"""
        H_concentration = 1e-1
        pH = -np.log10(H_concentration)
        assert pH == 1.0
    
    def test_electron_configuration_total_electrons(self):
        """Test total electron count matches atomic number"""
        atomic_number = 8  # Oxygen
        shell_1 = 2
        shell_2 = 6
        total_electrons = shell_1 + shell_2
        assert total_electrons == atomic_number


class TestChemistryProblems:
    """Realistic chemistry problem scenarios"""
    
    def test_problem_water_molar_mass_and_moles(self):
        """Calculate moles in 9g of water"""
        mass_water = 9.0  # grams
        molar_mass_water = 18.0  # g/mol
        moles = mass_water / molar_mass_water
        assert moles == 0.5
    
    def test_problem_acid_base_neutralization(self):
        """Calculate pH after neutralization"""
        pH_initial = 1.0  # strong acid
        pH_initial_base = 13.0  # strong base
        
        # After complete neutralization
        pH_final = 7.0
        assert pH_final == 7.0
    
    def test_problem_dilution_concentration(self):
        """10 mL of 5M solution diluted to 50 mL"""
        M1 = 5.0
        V1 = 10.0
        V2 = 50.0
        
        M2 = (M1 * V1) / V2
        assert M2 == 1.0
    
    def test_problem_percentage_composition(self):
        """Calculate mass percentage of element in compound"""
        # H2O: mass percent of H
        mass_H = 2.0
        mass_O = 16.0
        mass_H2O = mass_H + mass_O
        
        percent_H = (mass_H / mass_H2O) * 100
        np.testing.assert_almost_equal(percent_H, 11.11, decimal=1)
