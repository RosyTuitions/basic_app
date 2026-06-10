"""
Test suite for biology numerical problems - Class 12 PCB
Tests cellular biology, photosynthesis, respiration, and genetics
Based on: posts/cheatsheet_biology.md
"""

import pytest
import numpy as np


class TestPhotosynthesisNumericals:
    """Test photosynthesis calculations"""
    
    def test_photosynthesis_equation_balance(self):
        """Test photosynthesis: 6CO2 + 6H2O + light -> C6H12O6 + 6O2"""
        # Input reactants
        co2_molecules = 6
        h2o_molecules = 6
        
        # Output products
        glucose_molecules = 1
        o2_molecules = 6
        
        # Verify stoichiometry
        assert co2_molecules == 6
        assert h2o_molecules == 6
        assert glucose_molecules == 1
        assert o2_molecules == 6
    
    def test_glucose_production_from_co2(self):
        """Test glucose molecules produced from CO2"""
        # 6 CO2 -> 1 Glucose
        co2_available = 60
        glucose_produced = co2_available / 6
        assert glucose_produced == 10
    
    def test_oxygen_production_stoichiometry(self):
        """Test O2 produced in photosynthesis"""
        # 6 CO2 produces 6 O2
        co2_molecules = 6
        o2_produced = co2_molecules
        assert o2_produced == 6
    
    def test_water_consumption_photosynthesis(self):
        """Test water consumption in photosynthesis"""
        # 6 H2O consumed for 1 Glucose
        glucose_produced = 5
        water_needed = glucose_produced * 6
        assert water_needed == 30


class TestCellularRespirationNumericals:
    """Test cellular respiration calculations"""
    
    def test_respiration_equation_balance(self):
        """Test: C6H12O6 + 6O2 -> 6CO2 + 6H2O + ATP"""
        # Input
        glucose_molecules = 1
        o2_molecules = 6
        
        # Output
        co2_produced = 6
        h2o_produced = 6
        
        assert glucose_molecules == 1
        assert o2_molecules == 6
        assert co2_produced == 6
        assert h2o_produced == 6
    
    def test_atp_production_per_glucose(self):
        """Test ATP molecules produced per glucose"""
        # Typical: 1 glucose produces 30-32 ATP
        glucose = 1
        atp_produced_min = 30
        atp_produced_max = 32
        
        assert atp_produced_min <= 32 <= atp_produced_max
    
    def test_glycolysis_atp_production(self):
        """Test ATP production in glycolysis"""
        # Glycolysis: 1 glucose -> 2 ATP (net)
        glucose = 1
        atp_from_glycolysis = 2
        assert atp_from_glycolysis == 2
    
    def test_krebs_cycle_atp_production(self):
        """Test ATP production in Krebs cycle"""
        # Krebs cycle produces ~6-8 ATP per glucose
        glucose = 1
        atp_from_krebs_min = 6
        atp_from_krebs_max = 8
        assert atp_from_krebs_min <= 8 <= atp_from_krebs_max
    
    def test_electron_transport_chain_atp(self):
        """Test ATP production in electron transport chain"""
        # ETC produces ~26-28 ATP per glucose
        glucose = 1
        atp_from_etc_min = 26
        atp_from_etc_max = 28
        assert atp_from_etc_min <= 28 <= atp_from_etc_max


class TestGeneticsNumericals:
    """Test genetics and DNA calculations"""
    
    def test_dna_base_pairing(self):
        """Test Chargaff's rules - A=T and G=C"""
        # DNA sample
        adenine = 30
        thymine = 30
        guanine = 20
        cytosine = 20
        
        assert adenine == thymine
        assert guanine == cytosine
    
    def test_total_base_percentage(self):
        """Test base percentage calculation"""
        adenine = 30
        thymine = 30
        guanine = 20
        cytosine = 20
        
        total_bases = adenine + thymine + guanine + cytosine
        percent_A = (adenine / total_bases) * 100
        percent_G = (guanine / total_bases) * 100
        
        np.testing.assert_almost_equal(percent_A, 30.0, decimal=1)
        np.testing.assert_almost_equal(percent_G, 20.0, decimal=1)
    
    def test_complementary_strand_formation(self):
        """Test DNA complementary strand"""
        # If one strand has: A-T-G-C
        # Complement should be:  T-A-C-G
        
        original_strand = {'A': 20, 'T': 10, 'G': 15, 'C': 5}
        complement_strand = {'T': 20, 'A': 10, 'C': 15, 'G': 5}
        
        assert original_strand['A'] == complement_strand['T']
        assert original_strand['T'] == complement_strand['A']
        assert original_strand['G'] == complement_strand['C']
        assert original_strand['C'] == complement_strand['G']
    
    def test_genetic_code_codons(self):
        """Test genetic code - 64 possible codons"""
        bases = 4  # A, U, G, C
        codon_length = 3
        total_codons = bases ** codon_length
        assert total_codons == 64
    
    def test_dna_nucleotide_count(self):
        """Test counting nucleotides in DNA"""
        # If we have 10 base pairs
        base_pairs = 10
        nucleotides_in_double_helix = base_pairs * 2
        assert nucleotides_in_double_helix == 20


class TestMendelianGeneticsNumericals:
    """Test Mendelian genetics calculations"""
    
    def test_monohybrid_cross_ratios(self):
        """Test Mendelian monohybrid cross ratios"""
        # Aa × Aa
        homozygous_dominant = 1
        heterozygous = 2
        homozygous_recessive = 1
        
        ratio = f"{homozygous_dominant}:{heterozygous}:{homozygous_recessive}"
        assert ratio == "1:2:1"
    
    def test_monohybrid_phenotypic_ratio(self):
        """Test phenotypic ratio in monohybrid cross"""
        # Aa × Aa gives 3 dominant : 1 recessive
        dominant_phenotype = 3
        recessive_phenotype = 1
        
        total = dominant_phenotype + recessive_phenotype
        percent_dominant = (dominant_phenotype / total) * 100
        
        np.testing.assert_almost_equal(percent_dominant, 75.0, decimal=1)
    
    def test_dihybrid_cross_ratio(self):
        """Test Mendelian dihybrid cross ratio"""
        # AaBb × AaBb
        phenotypic_ratio = [9, 3, 3, 1]  # 9:3:3:1
        total = sum(phenotypic_ratio)
        assert total == 16
    
    def test_test_cross_probability(self):
        """Test test cross probability"""
        # Aa × aa
        dominant_offspring = 0.5
        recessive_offspring = 0.5
        
        assert dominant_offspring == 0.5
        assert recessive_offspring == 0.5
    
    def test_carrier_frequency_hardy_weinberg(self):
        """Test Hardy-Weinberg equation: p² + 2pq + q² = 1"""
        p = 0.7  # frequency of dominant allele
        q = 0.3  # frequency of recessive allele
        
        p_squared = p ** 2
        two_pq = 2 * p * q
        q_squared = q ** 2
        
        total = p_squared + two_pq + q_squared
        np.testing.assert_almost_equal(total, 1.0, decimal=10)


class TestCellDivisionNumericals:
    """Test cell division calculations"""
    
    def test_mitosis_chromosome_number(self):
        """Test chromosome number after mitosis"""
        # Parent cell: 2n (diploid)
        parent_chromosomes = 46  # human
        
        # After mitosis: 2n (diploid)
        daughter_cell_chromosomes = 46
        
        assert daughter_cell_chromosomes == parent_chromosomes
    
    def test_meiosis_chromosome_reduction(self):
        """Test chromosome reduction in meiosis"""
        # Parent cell: 2n (diploid)
        parent_chromosomes = 46
        
        # After meiosis: n (haploid)
        gamete_chromosomes = parent_chromosomes / 2
        
        assert gamete_chromosomes == 23
    
    def test_cell_division_mitosis_daughter_cells(self):
        """Test number of daughter cells from mitosis"""
        parent_cells = 1
        daughter_cells = parent_cells * 2
        assert daughter_cells == 2
    
    def test_cell_division_meiosis_gametes(self):
        """Test number of gametes from meiosis"""
        parent_cell = 1
        gametes = parent_cell * 4
        assert gametes == 4
    
    def test_dna_replication_doubling(self):
        """Test DNA amount after replication"""
        original_dna_amount = 1
        after_replication = original_dna_amount * 2
        assert after_replication == 2


class TestPopulationGeneticsNumericals:
    """Test population genetics calculations"""
    
    def test_allele_frequency_calculation(self):
        """Test allele frequency calculation"""
        # Population: 100 individuals
        AA_individuals = 30
        Aa_individuals = 60
        aa_individuals = 10
        total_individuals = 100
        
        # Calculate allele frequencies
        total_alleles = total_individuals * 2
        A_alleles = (AA_individuals * 2) + Aa_individuals
        a_alleles = (aa_individuals * 2) + Aa_individuals
        
        freq_A = A_alleles / total_alleles
        freq_a = a_alleles / total_alleles
        
        np.testing.assert_almost_equal(freq_A + freq_a, 1.0, decimal=10)
    
    def test_genotype_frequency_calculation(self):
        """Test genotype frequency calculation"""
        total_population = 100
        AA = 25
        Aa = 50
        aa = 25
        
        freq_AA = AA / total_population
        freq_Aa = Aa / total_population
        freq_aa = aa / total_population
        
        total_freq = freq_AA + freq_Aa + freq_aa
        assert total_freq == 1.0


class TestBiologyNumericalStability:
    """Test numerical stability and edge cases"""
    
    def test_atp_energy_values(self):
        """Test ATP energy release calculations"""
        # 1 mole ATP releases ~30.5 kJ
        atp_molecules = 1
        energy_per_atp = 30.5  # kJ/mol
        total_energy = atp_molecules * energy_per_atp
        
        assert np.isfinite(total_energy)
        assert total_energy > 0
    
    def test_very_small_mutation_frequency(self):
        """Test mutation frequency calculations"""
        mutations = 1
        total_bases = 1e9
        mutation_frequency = mutations / total_bases
        
        assert np.isfinite(mutation_frequency)
        assert mutation_frequency > 0
    
    def test_cell_cycle_time_calculations(self):
        """Test cell cycle duration calculations"""
        G1_phase = 8  # hours
        S_phase = 6   # hours
        G2_phase = 4  # hours
        M_phase = 2   # hours
        
        total_cycle = G1_phase + S_phase + G2_phase + M_phase
        assert total_cycle == 20


class TestBiologyProblems:
    """Realistic biology problem scenarios"""
    
    def test_problem_photosynthesis_glucose_yield(self):
        """Calculate glucose production from given CO2"""
        # 600 g CO2 used in photosynthesis
        mass_co2 = 600  # grams
        molar_mass_co2 = 44  # g/mol
        moles_co2 = mass_co2 / molar_mass_co2
        
        # 6 CO2 -> 1 Glucose
        molar_mass_glucose = 180  # g/mol
        moles_glucose = moles_co2 / 6
        mass_glucose = moles_glucose * molar_mass_glucose
        
        np.testing.assert_almost_equal(mass_glucose, 272.73, decimal=1)
    
    def test_problem_respiration_atp_yield(self):
        """Calculate ATP production from glucose"""
        glucose_molecules = 10
        atp_per_glucose = 30  # average
        total_atp = glucose_molecules * atp_per_glucose
        assert total_atp == 300
    
    def test_problem_genetic_cross_offspring(self):
        """Calculate offspring phenotype from cross"""
        # Cross: Aa (tall) × aa (short)
        # Expected ratio: 1:1
        dominant_offspring = 50  # percent
        recessive_offspring = 50  # percent
        
        assert dominant_offspring + recessive_offspring == 100
    
    def test_problem_mitosis_calculation(self):
        """Calculate cell number after mitosis rounds"""
        initial_cells = 1
        mitosis_rounds = 5
        final_cells = initial_cells * (2 ** mitosis_rounds)
        assert final_cells == 32
    
    def test_problem_population_allele_frequency(self):
        """Calculate allele frequency from genotype counts"""
        # Population: AA=300, Aa=500, aa=200
        AA = 300
        Aa = 500
        aa = 200
        total = 300 + 500 + 200
        
        A_alleles = (AA * 2) + Aa
        total_alleles = total * 2
        
        freq_A = A_alleles / total_alleles
        np.testing.assert_almost_equal(freq_A, 0.55, decimal=2)
