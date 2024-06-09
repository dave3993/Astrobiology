import numpy as np
from typing import List, Tuple
from astrobiology.directional_equations import (
    schwarzschild_radius, planck_energy, hawking_temperature,
    torque_equation, angular_momentum_equation, gravitational_time_dilation,
    luminosity_distance, compton_wavelength, de_broglie_wavelength, hubble_parameter,
    gravitational_redshift, synodic_period, lorentz_factor, escape_velocity,
    parsec_to_lightyear, chandrasekhar_limit, ecliptic_longitude, orbital_period,
    roche_limit, effective_temperature, doppler_shift, jean_mass, schrodinger_equation,
    redshift_velocity, specific_angular_momentum, radiative_pressure, critical_density,
    dynamical_time, virial_theorem, stellar_lifetime, escape_fraction, blackbody_spectrum,
    kepler_third_law, mach_number, virial_temperature, boltzmann_factor, hubble_law_velocity,
    gravitational_binding_energy, larmor_radius, magnetopause_radius, gravitational_wave_strain,
    taylor_series_expansion, particle_acceleration, lorentz_force, gravitational_wave_frequency,
    flux_density
)
from astrobiology.reward import calculate_score
from astrobiology.protocol import Predict

# Constants
M_sun = 1.989e30  # Solar mass in kg
G = 6.67430e-11   # Gravitational constant in m^3 kg^-1 s^-2
c = 299792458     # Speed of light in m/s
h = 6.62607015e-34 # Planck's constant in m^2 kg / s
k_B = 1.380649e-23 # Boltzmann constant in m^2 kg / s^2 K
sigma = 5.670374419e-8 # Stefan-Boltzmann constant in W m^-2 K^-4

def compute_schwarzschild_radius(predict: Predict) -> float:
    """
    Compute the Schwarzschild radius using the given mass of the asteroid.
    Adjust the initial radius by considering gravitational time dilation.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted Schwarzschild radius.
    """
    initial_radius = schwarzschild_radius(predict.asteroid_mass)
    adjusted_radius = gravitational_time_dilation(predict.asteroid_mass, initial_radius)
    return adjusted_radius

def compute_planck_energy(predict: Predict) -> float:
    """
    Compute the Planck energy using the given velocity constant.
    Adjust the initial energy by considering the Boltzmann factor.

    Args:
    predict (Predict): The prediction object containing velocity constant.

    Returns:
    float: The adjusted Planck energy.
    """
    initial_energy = planck_energy(predict.velocity_constant)
    adjusted_energy = boltzmann_factor(initial_energy, predict.temperature)
    return adjusted_energy

def compute_hawking_temperature(predict: Predict, time) -> float:
    """
    Compute the Hawking temperature using the given mass and time.
    Adjust the initial temperature by considering gravitational redshift.

    Args:
    predict (Predict): The prediction object containing asteroid mass.
    time: The time parameter for the Hawking temperature calculation.

    Returns:
    float: The adjusted Hawking temperature.
    """
    initial_temp = hawking_temperature(predict.asteroid_mass, time)
    # temp_with_gravity = gravitational_redshift(predict.asteroid_mass, initial_temp)
    return initial_temp

def compute_detected_peaks(predict: Predict) -> int:
    """
    Compute the number of detected peaks by adjusting the initial count
    using the Lorentz factor.

    Args:
    predict (Predict): The prediction object containing previous coordinates.

    Returns:
    int: The adjusted number of detected peaks.
    """
    peaks = len(predict.previous_coordinates)
    adjusted_peaks = int(peaks * lorentz_factor(predict.velocity_constant))
    return adjusted_peaks

def compute_strain_amplitude(predict: Predict) -> float:
    """
    Compute the strain amplitude using velocity constant, gravity, and mass.
    Adjust the strain using gravitational wave strain.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted strain amplitude.
    """
    strain = predict.velocity_constant * predict.gravity / predict.asteroid_mass
    strain_adjusted = gravitational_wave_strain(strain, predict.velocity_constant)
    return strain_adjusted

def compute_total_energy(predict: Predict) -> float:
    """
    Compute the total energy by summing kinetic and potential energy.
    Kinetic energy is calculated from mass and velocity, while potential energy
    is derived from gravitational potential.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The total energy.
    """
    kinetic_energy = 0.5 * predict.asteroid_mass * (predict.velocity_constant**2)
    potential_energy = -G * predict.asteroid_mass / predict.radius
    return kinetic_energy + potential_energy

def compute_main_sequence_lifetime(predict: Predict) -> float:
    """
    Compute the main sequence lifetime using stellar lifetime and Hubble parameter.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted main sequence lifetime.
    """
    lifetime = stellar_lifetime(predict.asteroid_mass, predict.luminosity)
    adjusted_lifetime = lifetime * hubble_parameter(predict.velocity_constant)
    return adjusted_lifetime

def compute_white_dwarf_radius(predict: Predict) -> float:
    """
    Compute the white dwarf radius using Chandrasekhar limit and Compton wavelength.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted white dwarf radius.
    """
    radius = chandrasekhar_limit(predict.asteroid_mass, predict.velocity_constant)
    adjusted_radius = radius * compton_wavelength(predict.asteroid_mass)
    return adjusted_radius

def compute_neutron_star_radius(predict: Predict) -> float:
    """
    Compute the neutron star radius using gravitational wave strain and Lorentz factor.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted neutron star radius.
    """
    radius = gravitational_wave_strain(predict.asteroid_mass, predict.velocity_constant)
    adjusted_radius = radius / lorentz_factor(predict.velocity_constant)
    return adjusted_radius

def compute_luminosity(predict: Predict) -> float:
    """
    Compute the luminosity using Stefan-Boltzmann law and Boltzmann factor.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted luminosity.
    """
    effective_temp = effective_temperature(predict.asteroid_mass, predict.velocity_constant)
    luminosity = sigma * (effective_temp**4) * (predict.asteroid_mass**2)
    adjusted_luminosity = luminosity * boltzmann_factor(luminosity, predict.temperature)
    return adjusted_luminosity

def compute_supernova_energy(predict: Predict) -> float:
    """
    Compute the supernova energy using virial theorem and specific angular momentum.
    Adjust the energy by considering gravitational redshift.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted supernova energy.
    """
    virial_energy = virial_theorem(predict.asteroid_mass, predict.velocity_constant)
    angular_momentum = specific_angular_momentum(predict.asteroid_mass, predict.velocity_constant)
    energy = virial_energy * angular_momentum
    adjusted_energy = energy * gravitational_redshift(predict.asteroid_mass, energy)
    return adjusted_energy

def compute_final_core_mass(predict: Predict) -> float:
    """
    Compute the final core mass using Jean mass and escape velocity.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted final core mass.
    """
    core_mass = jean_mass(predict.asteroid_mass, predict.velocity_constant)
    adjusted_core_mass = core_mass * escape_velocity(predict.asteroid_mass, predict.radius)
    return adjusted_core_mass

def compute_final_envelope_mass(predict: Predict) -> float:
    """
    Compute the final envelope mass using Roche limit and critical density.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted final envelope mass.
    """
    envelope_mass = roche_limit(predict.asteroid_mass, predict.velocity_constant)
    adjusted_envelope_mass = envelope_mass / critical_density(predict.asteroid_mass, predict.radius)
    return adjusted_envelope_mass

def compute_planck_spectrum(predict: Predict) -> float:
    """
    Compute the Planck spectrum using blackbody spectrum and Hubble parameter.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted Planck spectrum.
    """
    spectrum = blackbody_spectrum(predict.asteroid_mass, predict.velocity_constant)
    adjusted_spectrum = spectrum * hubble_parameter(predict.velocity_constant)
    return adjusted_spectrum

def compute_cmb_power_spectrum(predict: Predict) -> float:
    """
    Compute the CMB power spectrum using gravitational wave frequency and flux density.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted CMB power spectrum.
    """
    power_spectrum = gravitational_wave_frequency(predict.asteroid_mass, predict.velocity_constant)
    adjusted_power_spectrum = power_spectrum * flux_density(predict.asteroid_mass)
    return adjusted_power_spectrum

def compute_angular_diameter_distance(predict: Predict) -> float:
    """
    Compute the angular diameter distance using luminosity distance and parsec to lightyear conversion.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted angular diameter distance.
    """
    lum_distance = luminosity_distance(predict.asteroid_mass, predict.velocity_constant)
    hubble_param = hubble_parameter(predict.velocity_constant)
    distance = lum_distance / hubble_param
    adjusted_distance = distance * parsec_to_lightyear(distance)
    return adjusted_distance

def compute_sound_horizon(predict: Predict) -> float:
    """
    Compute the sound horizon using blackbody spectrum and virial temperature.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted sound horizon.
    """
    sound_horizon = blackbody_spectrum(predict.asteroid_mass, predict.velocity_constant)
    adjusted_horizon = sound_horizon * virial_temperature(predict.asteroid_mass)
    return adjusted_horizon

def compute_reionization_history(predict: Predict) -> float:
    """
    Compute the reionization history using Lorentz factor and escape fraction.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted reionization history.
    """
    history = predict.lorentz_factor * 0.5
    adjusted_history = history * escape_fraction(predict.asteroid_mass)
    return adjusted_history

def compute_dark_matter_density_profile(predict: Predict) -> float:
    """
    Compute the dark matter density profile using gravity and critical density.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted dark matter density profile.
    """
    density_profile = predict.gravity * 0.3 / predict.velocity_constant
    adjusted_profile = density_profile * critical_density(predict.asteroid_mass, predict.radius)
    return adjusted_profile

def compute_rotation_curve_velocity(predict: Predict) -> float:
    """
    Compute the rotation curve velocity using velocity constant and Mach number.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted rotation curve velocity.
    """
    velocity = predict.velocity_constant * 200 / predict.gravity
    adjusted_velocity = velocity * mach_number(predict.velocity_constant)
    return adjusted_velocity

def compute_dark_matter_mass_within_radius(predict: Predict) -> float:
    """
    Compute the dark matter mass within radius using gravitational binding energy.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted dark matter mass within radius.
    """
    mass_within_radius = predict.asteroid_mass * 1e12 / M_sun
    adjusted_mass = mass_within_radius * gravitational_binding_energy(predict.asteroid_mass, predict.radius)
    return adjusted_mass

def compute_lensing_deflection_angle(predict: Predict) -> float:
    """
    Compute the lensing deflection angle using gravity and Hubble law velocity.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted lensing deflection angle.
    """
    angle = predict.gravity * 1.0 / predict.velocity_constant
    adjusted_angle = angle * hubble_law_velocity(predict.asteroid_mass)
    return adjusted_angle

def compute_transit_depth(predict: Predict) -> float:
    """
    Compute the transit depth using mass and Lorentz force.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted transit depth.
    """
    depth = predict.asteroid_mass * 0.01 / M_sun
    adjusted_depth = depth * lorentz_force(predict.velocity_constant, predict.asteroid_mass)
    return adjusted_depth

def compute_radial_velocity_amplitude(predict: Predict) -> float:
    """
    Compute the radial velocity amplitude using velocity constant and Larmor radius.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted radial velocity amplitude.
    """
    amplitude = predict.velocity_constant * 10 / predict.gravity
    adjusted_amplitude = amplitude * larmor_radius(predict.asteroid_mass, predict.velocity_constant)
    return adjusted_amplitude

def compute_habitable_zone_inner(predict: Predict) -> float:
    """
    Compute the inner boundary of the habitable zone using Lorentz factor.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted inner boundary of the habitable zone.
    """
    return 0.95 * lorentz_factor(predict.velocity_constant)

def compute_habitable_zone_outer(predict: Predict) -> float:
    """
    Compute the outer boundary of the habitable zone using Lorentz factor.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted outer boundary of the habitable zone.
    """
    return 1.37 * lorentz_factor(predict.velocity_constant)

def compute_planet_equilibrium_temperature(predict: Predict) -> float:
    """
    Compute the planet equilibrium temperature using escape fraction.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted planet equilibrium temperature.
    """
    temperature = 288 * (1 - escape_fraction(predict.asteroid_mass))
    return temperature

def compute_transit_duration(predict: Predict) -> float:
    """
    Compute the transit duration using gravitational redshift.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.

    Returns:
    float: The adjusted transit duration.
    """
    duration = 0.5 * gravitational_redshift(predict.asteroid_mass, predict.velocity_constant)
    return duration

def compute_correct_values(predict: Predict, time) -> dict:
    """
    Compute the correct values for reward calculation based on the current state of the asteroid.

    Args:
    predict (Predict): The prediction object containing asteroid parameters.
    time: The time parameter for the calculations.

    Returns:
    dict: A dictionary of computed correct values.
    """
    print("Starting computation of correct values...")
    correct_values = {
        "schwarzschild_radius": compute_schwarzschild_radius(predict),
        "planck_energy": compute_planck_energy(predict),
        "hawking_temperature": compute_hawking_temperature(predict, time),
        "detected_peaks": compute_detected_peaks(predict),
        "strain_amplitude": compute_strain_amplitude(predict),
        "total_energy": compute_total_energy(predict),
        "main_sequence_lifetime": compute_main_sequence_lifetime(predict),
        "white_dwarf_radius": compute_white_dwarf_radius(predict),
        "neutron_star_radius": compute_neutron_star_radius(predict),
        "luminosity": compute_luminosity(predict),
        "supernova_energy": compute_supernova_energy(predict),
        "final_core_mass": compute_final_core_mass(predict),
        "final_envelope_mass": compute_final_envelope_mass(predict),
        "planck_spectrum": compute_planck_spectrum(predict),
        "cmb_power_spectrum": compute_cmb_power_spectrum(predict),
        "angular_diameter_distance": compute_angular_diameter_distance(predict),
        "sound_horizon": compute_sound_horizon(predict),
        "reionization_history": compute_reionization_history(predict),
        "dark_matter_density_profile": compute_dark_matter_density_profile(predict),
        "rotation_curve_velocity": compute_rotation_curve_velocity(predict),
        "dark_matter_mass_within_radius": compute_dark_matter_mass_within_radius(predict),
        "lensing_deflection_angle": compute_lensing_deflection_angle(predict),
        "transit_depth": compute_transit_depth(predict),
        "radial_velocity_amplitude": compute_radial_velocity_amplitude(predict),
        "habitable_zone_inner": compute_habitable_zone_inner(predict),
        "habitable_zone_outer": compute_habitable_zone_outer(predict),
        "planet_equilibrium_temperature": compute_planet_equilibrium_temperature(predict),
        "transit_duration": compute_transit_duration(predict),
    }
    return correct_values
