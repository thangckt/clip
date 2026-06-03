from clff import CLFF_ROOT
from clff.base import KEY as K
from thkit import THKIT_ROOT

EXAMPLE_PATH = "example"  # relative path to project_dir


def append_schema_text(md_file: str, yaml_schema_file: str):
    """Append yaml text to .md file."""
    with open(yaml_schema_file) as f:
        text = f.read()
    schema_text = "\n```yaml\n" + text + "\n```\n"
    schema_text = "\n## Schema:\n" + schema_text
    ### append yaml schema
    with open(md_file, "a") as f:
        f.write(schema_text)
    return


def append_example_config(md_file: str, config_files: list[str]):
    """Append yaml text to .md file."""
    for i, yaml_file in enumerate(config_files):
        with open(yaml_file) as f:
            text = f.read()
        schema_text = "\n```yaml\n" + text + "\n```\n"
        schema_text = f"\n## Example config {i + 1}:\n" + schema_text
        ### append yaml schema
        with open(md_file, "a") as f:
            f.write(schema_text)
    return


def main():
    ###ANCHOR Append schema to the .md files
    append_schema_text(
        md_file="./_docs/schema/manual_schema_gendata.md",
        yaml_schema_file=K.SCHEMA_GENDATA,
    )
    append_schema_text(
        md_file="./_docs/schema/manual_SCHEMA_CONCURRENTing.md",
        yaml_schema_file=K.SCHEMA_CONCURRENT,
    )
    append_schema_text(
        md_file="./_docs/schema/manual_schema_finetune.md",
        yaml_schema_file=K.SCHEMA_FINETUNE,
    )
    append_schema_text(
        md_file="./_docs/schema/manual_schema_phonon.md",
        yaml_schema_file=K.SCHEMA_PHONON,
    )
    append_schema_text(
        md_file="./_docs/schema/manual_schema_elastic.md",
        yaml_schema_file=K.SCHEMA_ELASTIC,
    )
    append_schema_text(
        md_file="./_docs/schema/manual_schema_pes_scan.md",
        yaml_schema_file=K.SCHEMA_PES_SCAN,
    )
    append_schema_text(
        md_file="./_docs/schema/manual_schema_ase_build.md",
        yaml_schema_file=K.SCHEMA_ASE_BUILD,
    )
    append_schema_text(
        md_file="./_docs/schema/manual_schema_ase_run.md",
        yaml_schema_file=K.SCHEMA_ASE_RUN,
    )
    append_schema_text(
        md_file="./_docs/schema/manual_schema_lammps.md",
        yaml_schema_file=K.SCHEMA_LAMMPS,
    )

    ### MLP schema
    append_schema_text(
        md_file="./_docs/schema/mlp_schema/mlp_schema_sevenn.md",
        yaml_schema_file=f"{CLFF_ROOT}/cl/mlp/schema_sevenn.yml",
    )

    ###ANCHOR Append example configuration to the .md files
    append_example_config(
        md_file="./_docs/schema/manual_schema_gendata.md",
        config_files=[f"{EXAMPLE_PATH}/gdata/sampleConfig_gendata.yml"],
    )
    append_example_config(
        md_file="./_docs/schema/manual_SCHEMA_CONCURRENTing.md",
        config_files=[f"{EXAMPLE_PATH}/al/sampleConfig_active_learn.yml"],
    )
    append_example_config(
        md_file="./_docs/schema/manual_schema_finetune.md",
        config_files=[f"{EXAMPLE_PATH}/al/sampleConfig_finetune.yml"],
    )

    append_example_config(
        md_file="./_docs/schema/manual_schema_phonon.md",
        config_files=[
            f"{EXAMPLE_PATH}/phonon/sampleConfig_phonon_gpaw.yml",
            f"{EXAMPLE_PATH}/phonon/sampleConfig_phonon_lammps.yml",
        ],
    )

    append_example_config(
        md_file="./_docs/schema/manual_schema_pes_scan.md",
        config_files=[
            f"{EXAMPLE_PATH}/pes/sampleConfig_pes_scan_gpaw.yml",
            f"{EXAMPLE_PATH}/pes/sampleConfig_pes_scan_lammps.yml",
        ],
    )

    append_example_config(
        md_file="./_docs/schema/manual_schema_ase_run.md",
        config_files=[f"{EXAMPLE_PATH}/script/sampleConfig_ase_run.yml"],
    )
    append_example_config(
        md_file="./_docs/schema/manual_schema_ase_build.md",
        config_files=[f"{EXAMPLE_PATH}/script/sampleConfig_ase_build.yml"],
    )
    append_example_config(
        md_file="./_docs/schema/manual_schema_lammps.md",
        config_files=[f"{EXAMPLE_PATH}/script/sampleConfig_lammps.yml"],
    )

    ###ANCHOR Schema from thkit package
    append_schema_text(
        md_file="./_docs/schema/manual_schema_machine.md",
        yaml_schema_file=f"{THKIT_ROOT}/jobman/schema/schema_machine.yml",
    )
    append_example_config(
        config_files=[f"{THKIT_ROOT}/jobman/schema/sampleConfig_machine_single.yml"],
        md_file="./_docs/schema/manual_schema_machine.md",
    )
    return


if __name__ == "__main__":
    main()
