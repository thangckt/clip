# clip

[CLIP](https://thangckt.github.io/clip/): Automated Frameworks for Concurrent Learning Interatomic Potentials and Material Properties Calculation.

![](https://thangckt.github.io/clip/_assets/image/logo_clip.svg)

CLIP is designed to automatically generate graph-based interactomic potentials through iterative active learning cycles (ML training → MD exploration → DFT labeling). The workflow is fully modular and highly customizable, enabling the entire process to run end-to-end without any user intervention. Key features of clip include:

- Automatic generation of necessary scripts for ML training, MD simulations, and DFT calculations.
- Submission of jobs to remote clusters, support almost connection protocols (e.g., Local, SSH, Cloud APIs,...), job schedulers (e.g., SLURM, SGE, PBS, TORQUE,...), and heterogeneous computing resources.
- Automated monitoring of job status and retrieval of results upon completion.
- Parsing of results and execution of active learning iterations automatically.
- Candidate-selection criteria based on energy, forces, (and/or) stresses.
- Easily configure sampling spaces, including (and/or) temperatures, stresses, enhanced samplings, van der Waals correction.
- Support multiple MD/DFT calculators.
- Support several leading graph-based MLIP models, and easy to implement any type of other MLIP models.

A distinctive capability of clip is its support for distributing workloads across multiple remote clusters. Rather than relying on a single cluster with long queue times, clip can asynchronously submit, monitor, and collect results from several heterogeneous computing infrastructures, dramatically accelerating the active learning workflow. Imagine combining computing resources from entirely different sources - such as Google Cloud, Amazon Web Services, national supercomputing centers, local campus clusters - and having them collaborate seamlessly within a single workflow? This is exactly what clip is designed for.

Or consider a practical scenario in which thousands of atomic structures must be labeled using DFT calculations on two heterogeneous clusters, one equipped with GPUs nodes + CPUs nodes + SLURM scheduler, and the other with only CPU nodes + SGE scheduler. You may want run half of the DFT jobs on the first cluster's GPUs nodes, a quarter on its CPUs nodes, and the remaining quarter on the second cluster's CPU nodes, simultaneously. clip easily handles this complex job distribution. With simple configurations, clip automatically distributes, schedules, and manages all jobs across the available resources without any manual intervention.

The modular design allows clip to easily extend/implement new functionalities/workflows. It already includes many built-in workflows to automatically compute Phonon dispersion, Potential energy surface (PES), elastic constants tensor, and more will be added.

The only task required from users is to provide a configuration file - then fasten the seatbelt and enjoy the ride.

<img src="https://thangckt.github.io/clip/manual/_image/intro_clip_1.png" style="display: block; margin-left: auto; margin-right: auto; max-width: 1000px;">

<img src="https://thangckt.github.io/clip/manual/_image/intro_clip_2.png" style="display: block; margin-left: auto; margin-right: auto; max-width: 1000px;">
