"""
Test suite for physics numerical problems - Class 12 PCB
Tests Newton's Laws, Motion, Energy, Waves, Electricity & Magnetism, and Light
Based on: posts/cheatsheet_physics.md
"""

import pytest
import numpy as np
from typing import Tuple


class TestMechanicsNumericals:
    """Test Newton's Laws and basic mechanics"""
    
    def test_newtons_second_law_force(self):
        """Test F = ma calculation"""
        mass = 2.0  # kg
        acceleration = 5.0  # m/s²
        force = mass * acceleration
        assert force == 10.0
    
    def test_newtons_second_law_acceleration(self):
        """Test a = F/m calculation"""
        force = 20.0  # Newton
        mass = 4.0  # kg
        acceleration = force / mass
        assert acceleration == 5.0
    
    def test_newtons_second_law_mass(self):
        """Test m = F/a calculation"""
        force = 30.0  # Newton
        acceleration = 6.0  # m/s²
        mass = force / acceleration
        assert mass == 5.0
    
    def test_multiple_forces_net_force(self):
        """Test net force calculation with multiple forces"""
        force1 = 10.0  # Right
        force2 = 5.0   # Left
        net_force = force1 - force2
        mass = 2.0
        
        acceleration = net_force / mass
        assert acceleration == 2.5


class TestMotionNumericals:
    """Test velocity, acceleration, and displacement"""
    
    def test_velocity_calculation(self):
        """Test v = d/t"""
        distance = 100.0  # meters
        time = 5.0  # seconds
        velocity = distance / time
        assert velocity == 20.0
    
    def test_acceleration_calculation(self):
        """Test a = Δv/Δt"""
        initial_velocity = 0.0  # m/s
        final_velocity = 20.0  # m/s
        time = 4.0  # seconds
        acceleration = (final_velocity - initial_velocity) / time
        assert acceleration == 5.0
    
    def test_displacement_uniform_motion(self):
        """Test displacement with uniform velocity"""
        velocity = 10.0  # m/s
        time = 5.0  # seconds
        displacement = velocity * time
        assert displacement == 50.0
    
    def test_kinematic_equation_s_ut_half_at2(self):
        """Test s = ut + ½at²"""
        u = 0.0  # initial velocity m/s
        t = 5.0  # time seconds
        a = 2.0  # acceleration m/s²
        s = u * t + 0.5 * a * t ** 2
        assert s == 25.0
    
    def test_kinematic_equation_v_squared(self):
        """Test v² = u² + 2as"""
        u = 0.0  # initial velocity
        a = 2.0  # acceleration
        s = 25.0  # displacement
        v_squared = u ** 2 + 2 * a * s
        v = np.sqrt(v_squared)
        assert v == 10.0
    
    def test_free_fall_acceleration(self):
        """Test acceleration during free fall"""
        g = 9.8  # m/s²
        time = 2.0  # seconds
        initial_velocity = 0.0
        
        distance_fallen = initial_velocity * time + 0.5 * g * time ** 2
        np.testing.assert_almost_equal(distance_fallen, 19.6, decimal=1)


class TestEnergyNumericals:
    """Test kinetic energy, potential energy, and conservation"""
    
    def test_kinetic_energy_calculation(self):
        """Test KE = ½mv²"""
        mass = 2.0  # kg
        velocity = 10.0  # m/s
        ke = 0.5 * mass * velocity ** 2
        assert ke == 100.0
    
    def test_potential_energy_calculation(self):
        """Test PE = mgh"""
        mass = 5.0  # kg
        g = 9.8  # m/s²
        height = 10.0  # m
        pe = mass * g * height
        np.testing.assert_almost_equal(pe, 490.0, decimal=0)
    
    def test_kinetic_energy_from_velocity(self):
        """Test finding velocity from kinetic energy"""
        mass = 1.0  # kg
        ke = 50.0  # Joules
        velocity = np.sqrt(2 * ke / mass)
        np.testing.assert_almost_equal(velocity, 10.0, decimal=5)
    
    def test_energy_conservation_free_fall(self):
        """Test energy conservation in free fall"""
        mass = 1.0  # kg
        g = 10.0  # m/s² (simplified)
        h_initial = 20.0  # m
        v_initial = 0.0
        
        # Initial energy at height
        pe_initial = mass * g * h_initial
        ke_initial = 0.5 * mass * v_initial ** 2
        total_initial = pe_initial + ke_initial
        
        # At ground level
        h_final = 0.0
        v_final = np.sqrt(2 * g * h_initial)
        pe_final = mass * g * h_final
        ke_final = 0.5 * mass * v_final ** 2
        total_final = pe_final + ke_final
        
        # Verify energy conservation
        np.testing.assert_almost_equal(total_initial, total_final, decimal=1)
    
    def test_work_energy_theorem(self):
        """Test W = ΔKE"""
        mass = 2.0  # kg
        v_initial = 0.0
        v_final = 10.0  # m/s
        
        ke_initial = 0.5 * mass * v_initial ** 2
        ke_final = 0.5 * mass * v_final ** 2
        work = ke_final - ke_initial
        assert work == 100.0
    
    def test_no_negative_energy(self):
        """Test that kinetic and potential energy are never negative"""
        velocities = np.array([0, 1, 5, 10, 100])
        heights = np.array([0, 1, 5, 10, 100])
        
        for v in velocities:
            ke = 0.5 * 1.0 * v ** 2
            assert ke >= 0, f"Negative KE for velocity {v}"
        
        for h in heights:
            pe = 1.0 * 9.8 * h
            assert pe >= 0, f"Negative PE for height {h}"


class TestWaveNumericals:
    """Test wave properties and calculations"""
    
    def test_wave_speed_calculation(self):
        """Test v = f × λ"""
        frequency = 50  # Hz
        wavelength = 6  # meters
        wave_speed = frequency * wavelength
        assert wave_speed == 300
    
    def test_frequency_from_wavelength(self):
        """Test f = v/λ"""
        wave_speed = 340  # m/s (sound in air)
        wavelength = 1.7  # m
        frequency = wave_speed / wavelength
        np.testing.assert_almost_equal(frequency, 200.0, decimal=0)
    
    def test_wavelength_from_frequency(self):
        """Test λ = v/f"""
        wave_speed = 3e8  # m/s (light speed)
        frequency = 6e14  # Hz
        wavelength = wave_speed / frequency
        np.testing.assert_almost_equal(wavelength, 5e-7, decimal=9)
    
    def test_sound_wave_speed_in_air(self):
        """Test sound wave calculations"""
        sound_speed = 340  # m/s at room temperature
        frequency = 1000  # Hz (human hearing)
        wavelength = sound_speed / frequency
        assert wavelength == 0.34
    
    def test_light_wave_frequency(self):
        """Test light frequency calculation"""
        c = 3e8  # speed of light m/s
        wavelength_red = 7e-7  # red light
        frequency_red = c / wavelength_red
        np.testing.assert_almost_equal(frequency_red, 4.29e14, decimal=12)
    
    def test_period_frequency_relationship(self):
        """Test T = 1/f"""
        frequency = 50  # Hz
        period = 1 / frequency
        assert period == 0.02


class TestElectricityMagnetismNumericals:
    """Test electricity and magnetism calculations"""
    
    def test_ohms_law_voltage(self):
        """Test V = IR"""
        current = 2.0  # Amperes
        resistance = 5.0  # Ohms
        voltage = current * resistance
        assert voltage == 10.0
    
    def test_ohms_law_current(self):
        """Test I = V/R"""
        voltage = 12.0  # Volts
        resistance = 4.0  # Ohms
        current = voltage / resistance
        assert current == 3.0
    
    def test_ohms_law_resistance(self):
        """Test R = V/I"""
        voltage = 20.0  # Volts
        current = 4.0  # Amperes
        resistance = voltage / current
        assert resistance == 5.0
    
    def test_electrical_power_calculation(self):
        """Test P = VI"""
        voltage = 10.0  # Volts
        current = 2.0  # Amperes
        power = voltage * current
        assert power == 20.0
    
    def test_electrical_power_from_resistance(self):
        """Test P = I²R"""
        current = 2.0  # Amperes
        resistance = 5.0  # Ohms
        power = current ** 2 * resistance
        assert power == 20.0
    
    def test_electrical_power_from_voltage(self):
        """Test P = V²/R"""
        voltage = 10.0  # Volts
        resistance = 5.0  # Ohms
        power = voltage ** 2 / resistance
        assert power == 20.0
    
    def test_electrical_energy(self):
        """Test E = Pt"""
        power = 100.0  # Watts
        time = 3600.0  # seconds (1 hour)
        energy = power * time
        assert energy == 360000.0  # Joules
    
    def test_series_resistance(self):
        """Test R_total = R1 + R2 + R3"""
        R1 = 2.0
        R2 = 3.0
        R3 = 5.0
        R_total = R1 + R2 + R3
        assert R_total == 10.0
    
    def test_parallel_resistance(self):
        """Test 1/R_total = 1/R1 + 1/R2"""
        R1 = 2.0
        R2 = 3.0
        R_total = 1 / (1/R1 + 1/R2)
        np.testing.assert_almost_equal(R_total, 1.2, decimal=5)
    
    def test_charge_calculation(self):
        """Test Q = I × t"""
        current = 2.0  # Amperes
        time = 300.0  # seconds
        charge = current * time
        assert charge == 600.0  # Coulombs


class TestLightNumericals:
    """Test light and optics calculations"""
    
    def test_speed_of_light(self):
        """Test light speed constant"""
        c = 3e8  # m/s
        assert c == 3e8
    
    def test_refractive_index(self):
        """Test refractive index calculation"""
        c = 3e8  # speed of light in vacuum
        v = 2e8  # speed of light in medium
        n = c / v
        assert n == 1.5
    
    def test_snells_law(self):
        """Test n1 × sin(θ1) = n2 × sin(θ2)"""
        n1 = 1.0  # air
        theta1 = 30.0  # degrees
        n2 = 1.5  # glass
        
        theta1_rad = np.radians(theta1)
        sin_theta2 = (n1 * np.sin(theta1_rad)) / n2
        theta2_rad = np.arcsin(sin_theta2)
        theta2 = np.degrees(theta2_rad)
        
        np.testing.assert_almost_equal(theta2, 19.47, decimal=1)
    
    def test_lens_formula(self):
        """Test 1/f = 1/u + 1/v"""
        focal_length = 10.0  # cm
        object_distance = 20.0  # cm
        
        # Calculate image distance
        one_over_v = (1 / focal_length) - (1 / object_distance)
        image_distance = 1 / one_over_v
        
        assert image_distance == 20.0
    
    def test_lens_magnification(self):
        """Test m = v/u"""
        image_distance = 30.0  # cm
        object_distance = 10.0  # cm
        magnification = image_distance / object_distance
        assert magnification == 3.0


class TestNumericalStability:
    """Test numerical stability and edge cases"""
    
    def test_no_nan_infinity_in_calculations(self):
        """Verify calculations don't produce NaN or Infinity"""
        mass = 1.0
        velocity = 1e6
        acceleration = 9.8
        
        ke = 0.5 * mass * velocity ** 2
        force = mass * acceleration
        
        assert np.isfinite(force), "Force calculation produced non-finite value"
        assert np.isfinite(ke), "KE calculation produced non-finite value"
    
    def test_floating_point_precision(self):
        """Test floating point comparisons with appropriate tolerance"""
        result = 0.1 + 0.2
        expected = 0.3
        
        np.testing.assert_allclose(result, expected, rtol=1e-10)
    
    def test_division_by_zero_handling(self):
        """Test handling of edge cases like division by zero"""
        with pytest.raises(ZeroDivisionError):
            _ = 10 / 0
    
    def test_very_large_numbers(self):
        """Test calculations with very large numbers"""
        mass = 1e30  # kg
        velocity = 1e8  # m/s
        ke = 0.5 * mass * velocity ** 2
        
        assert np.isfinite(ke)
        assert ke > 0
    
    def test_very_small_numbers(self):
        """Test calculations with very small numbers"""
        mass = 1e-30  # kg
        velocity = 1  # m/s
        ke = 0.5 * mass * velocity ** 2
        
        assert np.isfinite(ke)
        assert ke >= 0


class TestPhysicsProblems:
    """Realistic physics problem scenarios"""
    
    def test_problem_ball_dropped_from_height(self):
        """A ball is dropped from 100m height. Find velocity when it hits ground."""
        h = 100.0  # meters
        g = 9.8  # m/s²
        u = 0.0  # initial velocity
        
        # v² = u² + 2gh
        v_squared = u ** 2 + 2 * g * h
        v = np.sqrt(v_squared)
        
        np.testing.assert_almost_equal(v, 44.27, decimal=1)
    
    def test_problem_projectile_motion_range(self):
        """Find horizontal range of projectile launched at 45°"""
        v0 = 20  # initial velocity m/s
        angle = 45  # degrees
        g = 9.8  # m/s²
        
        angle_rad = np.radians(angle)
        # Range = (v0² × sin(2θ)) / g
        range_distance = (v0 ** 2 * np.sin(2 * angle_rad)) / g
        
        np.testing.assert_almost_equal(range_distance, 40.82, decimal=1)
    
    def test_problem_circular_motion(self):
        """Find centripetal acceleration for circular motion"""
        velocity = 10  # m/s
        radius = 5  # m
        
        # a = v²/r
        centripetal_accel = velocity ** 2 / radius
        assert centripetal_accel == 20.0
    
    def test_problem_simple_pendulum_period(self):
        """Find period of simple pendulum"""
        L = 1.0  # length in meters
        g = 9.8  # m/s²
        
        # T = 2π√(L/g)
        period = 2 * np.pi * np.sqrt(L / g)
        np.testing.assert_almost_equal(period, 2.0, decimal=1)
    
    def test_problem_two_resistors_series(self):
        """Two resistors in series with voltage source"""
        R1 = 10.0  # Ohms
        R2 = 20.0  # Ohms
        V = 30.0  # Volts
        
        R_total = R1 + R2
        current = V / R_total
        
        assert current == 1.0
        V1 = current * R1
        V2 = current * R2
        
        np.testing.assert_almost_equal(V1 + V2, 30.0, decimal=5)
