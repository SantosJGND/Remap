#!/bin/bash
# This script is used to set the environment variables for the utilities

"""

This script is used to set the environment variables for the utilities
"""


MEDIA_ROOT = "/tmp/televir/media/"
STATICFILES_DIRS = ["/tmp/televir/static/"]


from utilities.constants_settings import ConstantsSettings as CS


class Deployment_Params:

    SOURCE = {
        "ENVSDIR": "/home/bioinf/Desktop/METAGEN/db_third_test/mngs_environments/",
        "CONDA": "/opt/conda/",
        "DBDIR_MAIN": "/home/bioinf/Desktop/METAGEN/db_third_test/ref_db/",
        "REF_FASTA": "/home/bioinf/Desktop/METAGEN/db_third_test/ref_fasta/",
        "METAD": "/home/bioinf/Desktop/METAGEN/db_third_test/metadata/",
        "BIN": "/insaflu_web/TELEVIR/deployment_scripts/scripts/",
    }

    METADATA = {
        "ROOT": "/home/bioinf/Desktop/METAGEN/db_third_test/metadata/",
        "input_accession_to_taxid_path": "acc2taxid.tsv",
        "input_taxonomy_to_descriptor_path": "taxid2desc.tsv",
        "input_protein_accession_to_protid_path": "protein_acc2protid.tsv",
        "input_protein_accession_to_taxid_path": "protein_acc2taxid.tsv",
    }

    REFERENCE_MAIN = "/home/bioinf/Desktop/METAGEN/db_third_test/ref_fasta/"

    BINARIES = {
        "SOURCE": "/opt/conda/",
        "ROOT": "/home/bioinf/Desktop/METAGEN/db_third_test/mngs_environments/",
        "software": {
            CS.PIPELINE_NAME_contig_classification: "hostDepletion/hostdep_env",
            CS.PIPELINE_NAME_read_classification: "hostDepletion/hostdep_env",
            CS.PIPELINE_NAME_viral_enrichment: "hostDepletion/hostdep_env",
            "centrifuge": "hostDepletion/hostdep_env",
            "diamond": "hostDepletion/hostdep_env",
            "kaiju": "hostDepletion/hostdep_env",
            "krakenuniq": "hostDepletion/hostdep_env",
            "blast": "hostDepletion/hostdep_env",
            "kraken2": "kraken2/kraken_env",
            "fastviromeexplorer": "FastViromeExplorer/FastViromeExplorer",
            "kallisto": "FastViromeExplorer/fve",
            "virsorter": "hostDepletion/vs2",
            "desamba": "classm_lc/deSAMBA",
            "minimap-rem": "hostDepletion/hostdep_env",
            "flye": "assembly/Flye",
            "clark": "classification/Clark",
            "minimap2_ONT": "hostDepletion/hostdep_env",
            "minimap2_asm": "hostDepletion/hostdep_env",
            "blastn": "hostDepletion/hostdep_env",
            "blastp": "hostDepletion/hostdep_env",
            "snippy": "/software/snippy",
            "bwa": "remap/remap",
        },
        CS.PIPELINE_NAME_remapping: {"default": "remap/remap"},
        CS.PIPELINE_NAME_read_quality_analysis: {"default": "preprocess/preproc"},
        CS.PIPELINE_NAME_assembly: {"default": "assembly/assembly"},
    }

    DIRS = {
        CS.PIPELINE_NAME_read_quality_analysis: "reads/clean/",
        "reads_depleted_dir": "reads/hd_filtered/",
        "reads_enriched_dir": "reads/enriched/",
        CS.PIPELINE_NAME_host_depletion: "host_depletion/",
        CS.PIPELINE_NAME_viral_enrichment: "enrichment/",
        CS.PIPELINE_NAME_assembly: "assembly/",
        CS.PIPELINE_NAME_contig_classification: "classification/assembly/",
        CS.PIPELINE_NAME_read_classification: "classification/reads/",
        CS.PIPELINE_NAME_remapping: "remap/",
        "log_dir": "logs/",
        "OUTD": "output/",
    }

    ################################## MODULES

    ACTIONS = {
        "CLEAN": False,
        "QCONTROL": False,
        "ENRICH": True,
        "DEPLETE": False,
        "ASSEMBLE": False,
        "CLASSIFY": True,
        "REMAP": True,
        "PHAGE_DEPL": True,
        "VIRSORT": False,
        "SIFT": True,
    }


class Params_Illumina:
    """
    Parameters for the Illumina pipeline
    """

    DATA_TYPE = "illumina"

    ################################## CONSTANT PARAMS

    CONSTANTS = {
        "minimum_coverage_threshold": 2,
        "max_output_number": 100,
        "taxid_limit": 100,
        "sift_query": "phage",
        "assembly_contig_min_length": 300,
    }

    ################################## SOFTWARE


class Params_Nanopore:
    """
    Class containing all the parameters for the nanopore pipeline
    """

    DATA_TYPE = "nanopore"

    CONSTANTS = {
        "minimum_coverage_threshold": 1,
        "max_output_number": 15,
        "taxid_limit": 12,
        "sift_query": "phage",
        "assembly_contig_min_length": 500,
    }
