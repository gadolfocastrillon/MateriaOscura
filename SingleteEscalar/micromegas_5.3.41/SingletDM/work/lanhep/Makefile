
.PHONY: all

all: *.lhp ../../../Packages/LanHEP/lhep
	../../../Packages/LanHEP/lhep -ca -evl 2 singletDM.lhp

../../../Packages/LanHEP/lhep:
	$(MAKE) -C ../../../Packages/LanHEP
	