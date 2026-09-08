# Security Research Tools

Security research toolkit for vulnerability assessment, OSINT, and penetration testing on network infrastructure.

## Overview

This project contains tools and methodologies for authorized security research including:
- Network reconnaissance and service discovery
- RTSP/ONVIF vulnerability assessment
- Credential testing and brute-force optimization
- OSINT data collection and analysis
- Telecom infrastructure security assessment

## Tools Included

### 1. Parallel Brute Force Framework
Optimized Hydra-based parallel attack framework for efficient credential testing.

**Features:**
- Multi-threaded attack distribution
- Wordlist optimization and splitting
- Real-time progress monitoring
- Automatic session recovery
- Support for RTSP, SSH, MySQL, SMB protocols

**Usage:**
```bash
./hydra_parallel.sh <target_ip> <protocol> <wordlist>
```

### 2. OSINT & Recon Tools
- WHOIS lookup and IP range enumeration
- DNS reverse lookup
- Banner grabbing
- Service version detection
- Public record analysis

### 3. Wordlist Generation
Targeted password lists for specific industries/regions:
- Camera equipment defaults
- Telecom company patterns
- Regional/geographic variations
- Company-specific conventions

### 4. Analysis Scripts
- RTSP stream path enumeration
- Authentication protocol detection
- Service fingerprinting
- Vulnerability assessment automation

## Methodology

### Phase 1: Reconnaissance
1. WHOIS/DNS lookup to identify infrastructure owner
2. CIDR block enumeration for complete IP ranges
3. Port scanning for active services
4. Banner grabbing for version detection

**Example:**
```bash
whois example_ip_block
nmap -sV -p- example_target_ip
```

### Phase 2: Vulnerability Assessment
1. Identify running services and versions
2. Check for known CVEs using exploit databases
3. Analyze authentication mechanisms
4. Test for default credentials and misconfigurations

### Phase 3: Social Engineering & OSINT
1. Organization information gathering
2. Employee/contact identification
3. Default credential research for specific vendors
4. Configuration pattern analysis

### Phase 4: Authorized Testing
1. Brute force testing with optimized wordlists
2. Exploitation of identified vulnerabilities
3. Access validation and reporting

## Requirements

- Linux/Unix environment
- Hydra (THC-Hydra 9.x+)
- Python 3.6+
- curl, nmap, netcat
- Standard networking tools

## Installation

```bash
# Install dependencies
sudo apt-get install hydra nmap netcat curl

# Clone repository
git clone https://github.com/[username]/security-research-tools.git
cd security-research-tools

# Make scripts executable
chmod +x *.sh
```

## Usage

### Network Reconnaissance
```bash
# WHOIS lookup
whois example_target_subnet

# Port scanning
nmap -sV -p- target_ip

# Service detection
./rtsp_discovery.py target_subnet
```

### Brute Force Testing
```bash
# Single target
hydra -L users.txt -P wordlist.txt -s 554 target_ip rtsp -t 8

# Parallel multi-target
./hydra_parallel.sh
```

### OSINT Collection
```bash
# Company intelligence
python3 osint_recon.py "Company Name"

# IP range analysis
./whois_analysis.sh example_target_subnet/19
```

## Important Notes

⚠️ **Legal & Ethical Use**
- Use only on systems you own or have explicit written permission to test
- Always obtain authorization before conducting security assessments
- Follow responsible disclosure practices
- Comply with local laws and regulations
- Report findings to system owners through proper channels

## Responsible Disclosure

When vulnerabilities are discovered:
1. Document findings thoroughly
2. Notify affected organizations immediately
3. Allow reasonable time for patching (30-90 days)
4. Do not publicly disclose until patched
5. Provide technical recommendations

## Lessons Learned

### Optimization Techniques
- **Parallel Processing**: Distribute wordlists across multiple processes for 3-5x speedup
- **Targeted Wordlists**: Company/region-specific lists outperform generic wordlists
- **Rate Limiting**: Balance speed vs. detection avoidance
- **Session Recovery**: Save state to resume interrupted attacks

### Common Vulnerabilities Found
- Weak default credentials still in use
- Digest authentication implementation flaws
- Lack of rate limiting on authentication endpoints
- Missing security headers on management interfaces
- Unencrypted administrative protocols (RTSP, SNMP, HTTP)

## Tools Referenced

- [THC-Hydra](https://github.com/vanhauser-thc/thc-hydra) - Credential testing
- [Nmap](https://nmap.org/) - Network discovery
- [Shodan](https://www.shodan.io/) - Public service enumeration
- [OSINT Framework](https://osintframework.com/) - Information gathering

## Contributing

Security research contributions welcome:
- Additional protocol support
- Optimization improvements
- Detection evasion techniques (for authorized testing)

## License

Research and educational use only.

## Contact & Support

For security research inquiries and collaboration:
- Create issues for tool improvements
- Submit PRs for enhancements
- Document findings responsibly

---

**Last Updated:** September 2026  
**Status:** Active research project
