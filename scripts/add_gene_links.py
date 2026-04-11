#!/usr/bin/env python3
"""Add GeneCards links to the first occurrence of each gene name per chapter."""

import re
import os
import glob

# Curated gene names that appear in this book
GENE_NAMES = {
    # ASD / NDD core genes
    "CHD8", "SCN2A", "DYRK1A", "KATNAL2", "POGZ", "TBR1", "ANK2", "CUL3",
    "GRIN2B", "NRXN1", "SHANK2", "SHANK3", "SYNGAP1", "ADNP", "FOXP1",
    "FOXP2", "ARID1B", "KDM5C", "SETD5", "PTEN", "CHD4", "CHD7",
    "CNTNAP2", "NLGN3", "NLGN4", "ASH1L", "KMT2C", "AUTS2",
    "CDKN1A", "CDKN1C", "CDKN2A", "AFF3",
    # Epilepsy genes
    "SCN1A", "SCN8A", "KCNQ2", "KCNQ3", "KCNB1", "GABRA1", "GABRB3",
    # Alzheimer's
    "APOE", "TREM2",
    # Neural progenitor / cortical development TFs
    "PAX6", "SOX2", "FOXG1", "EMX1", "EMX2", "EOMES", "GLI3",
    "NEUROG2", "NEUROD1", "NEUROD2", "NEUROD6",
    "FEZF1", "FEZF2", "SATB2", "BCL11A", "BCL11B", "CUX1", "CUX2",
    "RORB", "TLE4", "SOX6", "PROX1",
    # Interneuron TFs
    "DLX2", "DLX5", "LHX6", "NKX2", "GSX2",
    # Signaling
    "FOXM1", "HES1", "HES4", "HES5", "HOPX",
    "PTBP1", "PTBP2", "RBFOX1", "RBFOX2", "RBFOX3",
    # Synaptic
    "GRIA1", "GRIN2A",
    # Oligodendrocyte
    "OLIG2", "MBP", "MOG", "MOBP",
    # Astrocyte
    "GFAP", "AQP4", "SLC1A2", "SLC1A3",
    # Microglia
    "TMEM119", "P2RY12", "CX3CR1", "CSF1R", "CLEC7A",
    # BBB / Vascular
    "CLDN5", "MFSD2A", "SLC2A1", "SLC7A5", "SLC7A1",
    "PDGFRB", "PDGFRA", "CSPG4",
    "ABCB1", "ABCG2", "TFRC",
    "COL4A1", "COL5A2", "ACTA2",
    "VEGFC", "NOS3", "PIEZO1", "PIEZO2",
    "OCLN", "PLVAP", "ESM1",
    # Neuronal markers
    "RELN", "DCX", "STMN2", "TUBB3", "CALB1", "CALB2",
    "PVALB", "SST", "VIP", "LAMP5", "SCGN",
    "SLC17A6", "SLC17A7", "SLC32A1", "GAD2",
    # Other important genes
    "BDNF", "FMR1", "BRAF", "HRAS",
    "TSC1", "TSC2", "PTPN11",
    "CACNA1C", "PCDH19",
    "LIS1", "SHOX2",
    "EZH2", "EED", "SUZ12",
    "DNMT1",
    "CTCF", "MEF2C", "MEIS2",
    "BRN2", "POU4F1", "FOXA2", "LMX1A", "LMX1B",
    "ERBB4", "CELSR1", "RFX3",
    "SOD1", "SOD2", "TP53",
    "NANOG",
    # Evolution / synapse
    "APPBP2", "ENOX2",
    # Organoid
    "BARHL2",
    # Other markers
    "NESTIN", "VIM",
    "FAM107A", "LIFR",
    "GJA1", "SPARC", "SPARCL1",
    "P2RX3",
    "CBLN1", "CBLN2",
    "NR4A1", "EGR1", "FOS", "ARC",
    "NFIA", "NFIB",
    "TBR2",  # also known as EOMES
    "CNTN4",
    "STMN1",
    "SYN1",
    "SPP1", "GPNMB", "PSAP",
    "LNPK", "AGMO", "ANO3", "HYAL2",
    "ST6GAL2", "TMEM158", "ZNF703",
    "ARL15", "SPHKAP", "PCSK7",
    "ITGB4", "ITGB8",
    "ARSA",
    "TSHZ2",
    "PPP1R17",
    "DARPP32", "PDE10A",
    "RNASEH2A",
    "DRD1", "DRD2",
    "CELF4", "ELAVL1",
    "PTPRZ1", "BCAN",
    "NPY", "TACR1",
    "MYL2", "SNCG",
    "ACKR1", "CD93", "CD9",
    "UNC5B", "PTN",
    "ADGRG6",
    "TRPV1", "TRPM8", "TRPA1", "TRPC3",
    "CRABP",
    "RUNX1", "MAFB",
    "SMARCC2",
    "GBX2", "OTX2", "EN1", "EN2",
    "PHOX2A", "DBX1",
    "TCF7L2", "TCF3",
    "DCLK1",
    "FGF8", "FZD8", "DKK2", "BMP7",
    "CCN2",
    "RPH3A",
    "INSR", "IGF1",
    "SIX1",
    "PRRX1",
    "MGMT",
}

# Abbreviations that should NOT be linked (not gene names in this context)
NOT_GENES = {
    "RNA", "DNA", "CRISPR", "GWAS", "BICCN", "ASD", "BBB", "VZ", "SVZ",
    "IPC", "IT", "ET", "CT", "DL", "PCW", "PSD", "WGCNA", "ISH", "UMAP",
    "CGE", "MGE", "LGE", "RBP", "WGS", "TAD", "FDR", "DEG", "iPSC",
    "FISH", "HIP", "AMY", "STR", "ATAC", "FGF", "BMP", "SHH", "WNT",
    "TGF", "MEK", "PI3K", "ERK", "MTOR", "SNP", "CNV", "LOF", "GOF",
    "FACS", "MERFISH", "OPC", "NSC", "AAV", "GFP", "NPC",
    "NMDA", "NMDAR", "AMPA", "GABA", "EEG", "MRI", "PET",
    "ENCODE", "HAR", "MPRA", "WES", "UMI", "ONT", "NDD",
    "DLPFC", "PFC", "OFC", "MFC", "DFC", "ITC", "V1C", "VFC",
    "CBC", "MD", "NVU", "VLMC", "VSMC",
    "BAF", "PAM", "ECM", "DMR", "DMG",
    "AI", "SPARK", "MSSNG",
    "PCR", "PCA", "SNF",
    "IBA1", "NG2",  # often used as markers/abbreviations
    "SMAD",  # signaling pathway name, not a single gene
    "HOX",  # gene family
    "FOX1",  # not a standard gene name
    "FMRP",  # protein, not gene (FMR1 is the gene)
    "SWI", "PRC2", "COMPASS",  # complexes
    "OSVZ", "IKNM",
    "NOCAP", "HNOCA",  # organoid names
    "LASSO",  # statistical method
    "RACE",  # method
    "DAM",  # disease-associated microglia
    "FANS", "LMD",
    "ISSCR",  # organization
    "UCLA", "NIH", "BMC", "MIT",
    "EBI", "OMIM", "UCSC",
    "DSM",
    "HLA", "MHC",
    "BOLD",
    "ROSMAP",
    "AUUUA", "GCAUG", "UGUGU",  # RNA motifs
    "TBR2",  # this is actually EOMES, and TBR2 is used as a marker name
}

GENECARD_URL = "https://www.genecards.org/cgi-bin/carddisp.pl?gene={}"


def add_links_to_chapter(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    lines = content.split('\n')
    linked_genes = set()
    new_lines = []
    in_references = False

    for line in lines:
        # Don't add links in reference section
        if line.strip().startswith('**References**') or line.strip() == '---':
            if '**References**' in line:
                in_references = True
        if in_references:
            new_lines.append(line)
            continue

        # Don't add links in headings
        if line.startswith('#'):
            new_lines.append(line)
            continue

        # Don't add links in table headers
        if line.startswith('|') and '---|' in line:
            new_lines.append(line)
            continue

        # Process the line for gene names
        for gene in sorted(GENE_NAMES - NOT_GENES, key=len, reverse=True):
            if gene in linked_genes:
                continue

            # Pattern: word boundary, gene name, word boundary
            # But not already inside a markdown link or followed by lowercase (part of longer word)
            pattern = r'(?<!\[)(?<!\w)(' + re.escape(gene) + r')(?!\w)(?!\]\()'

            match = re.search(pattern, line)
            if match:
                url = GENECARD_URL.format(gene)
                link = f'[{gene}]({url})'
                # Replace only the first occurrence in this line
                line = line[:match.start()] + link + line[match.end():]
                linked_genes.add(gene)

        new_lines.append(line)

    result = '\n'.join(new_lines)

    if result != content:
        with open(filepath, 'w') as f:
            f.write(result)
        return len(linked_genes)
    return 0


def main():
    chapters = sorted(glob.glob('part*/chapter*.md'))
    total = 0
    for ch in chapters:
        count = add_links_to_chapter(ch)
        if count > 0:
            print(f"{ch}: {count} genes linked")
        total += count
    print(f"\nTotal: {total} gene links added across {len(chapters)} chapters")


if __name__ == '__main__':
    main()
