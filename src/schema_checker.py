import argparse
import xmltodict


def main(args=None):
    p=make_parser()
    ns=p.parse_args(args=args)

    with open(ns.infile[0], "rb") as f:
        sim=xmltodict.parse(f)

    inst_facilities=set()

    # nullinst
    for item in dict_extract("initialfacilitylist",sim):
        if type(item['entry']) is dict:
            inst_facilities.add(item['entry']['prototype'])
        else:
            for entry in item['entry']:
                inst_facilities.add(entry['prototype'])
    # deployinst
    for item in dict_extract("DeployInst",sim):
        for entry in item['prototypes']:
            inst_facilities.add(entry['val'])

    defined_facilities = {fac["name"] for fac in sim["simulation"]["facility"]}

    missing_inst = defined_facilities.difference(inst_facilities)
    if len(missing_inst):
        print("These facilities are not deployed by NullInst: " + str(missing_inst))
    missing_fac = inst_facilities.difference(defined_facilities)
    if len(missing_fac):
        print("These facilities don't have a prototype defined: " + str(missing_fac))
    if not len(missing_fac) and not len(missing_inst):
        print("All defined facilities are deployed! Good work")

    return


def dict_extract(key,var):
    if hasattr(var,'items'):
        for k,v in var.items():
            if k==key:
                yield v
            if isinstance(v,dict):
                for result in dict_extract(key,v):
                    yield result
            elif isinstance(v,list):
                for d in v:
                    for result in dict_extract(key,d):
                        yield result


def make_parser():
    p=argparse.ArgumentParser()
    p.add_argument('infile', nargs=1, help="Cyclus input file to check")
    return p


if __name__ == '__main__':
    main()